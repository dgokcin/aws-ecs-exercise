# aws-ecs-exercise

## Task

Configuring an end to end deployment pipeline on AWS that manages the lifecycle
of a web application.

## Service

Due to its simplicity, I used Flask to develop the simple web application. The
web application is serving on port 5000 and it justs prints a hello message to the page.

## CI/CD

### GitHub Actions

### Amazon CodeBuild

### Amazon ECS

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration
service that makes it easy to operate containerized workloads at scale.  It also integrates
with other core AWS services, such as Amazon Route 53, AWS Identity and Access Management
(IAM), and Amazon CloudWatch.  Establishing an effective and efficient CI/CD
pipeline is critical for containerized applications, regardless of the platform
you are using to manage your containers.

#### aws-cli

#### aws-cdk

### Screenshots

#### Deploying the infrastructure with aws-cdk
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/cdk-deploy.png)
#### Triggering Amazon CodeBuild with a commit
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/git-sha.png)
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/code-build.png)

#### Building and pushing the current webapp to ECR
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/ecr-repositories.png)

#### Applying the task definition
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/github-actions-successful-pipeline.png)
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/checks.png)

#### The new version deployed with GitOps
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/gitops.png)


### References

- [AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
- [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)
- [AWS CDK Installation](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
