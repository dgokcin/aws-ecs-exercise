"""AWS CDK module to create ECS infrastructure"""
from aws_cdk import (core, aws_ecs as ecs, aws_ecr as ecr, aws_ec2 as ec2,
        aws_iam as iam, aws_ecs_patterns as ecs_patterns)

class EcsDevopsSandboxCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the ECR Repository
        ecr_repository = ecr.Repository(self,
                                        "ecs-devops-sandbox-repository",
                                        repository_name="ecs-devops-sandbox-repository")

        # Create the ECS Cluster (and VPC)
        vpc = ec2.Vpc(self,
                      "ecs-devops-sandbox-vpc",
                      max_azs=3)
        cluster = ecs.Cluster(self,
                              "ecs-devops-sandbox-cluster",
                              cluster_name="ecs-devops-sandbox-cluster",
                              vpc=vpc)

        # Create the ECS Task Definition with placeholder container (and named Task Execution IAM Role)
        execution_role = iam.Role(self,
                                  "ecs-devops-sandbox-execution-role",
                                  assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                                  role_name="ecs-devops-sandbox-execution-role")
        execution_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
                ]
        ))
        task_definition = ecs.FargateTaskDefinition(self,
                                                    "ecs-devops-sandbox-task-definition",
                                                    execution_role=execution_role,
                                                    family="ecs-devops-sandbox-task-definition")

        container = task_definition.add_container(
            "ecs-devops-sandbox",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
        )

        port_mapping = ecs.PortMapping(container_port=5000)
        container.add_port_mappings(port_mapping)


        # Create a load balanced ECS Service
        # Athough this block works, I was not able to
        load_balanced_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "ecs-devops-sandbox-service",
            cluster=cluster,
            task_definition=task_definition,
            service_name="ecs-devops-sandbox-service")

        #Create the ECS Service
        # service = ecs.FargateService(self,
                                     # "ecs-devops-sandbox-service",
                                     # cluster=cluster,
                                     # task_definition=task_definition,
                                     # assign_public_ip=True,
                                     # service_name="ecs-devops-sandbox-service")

