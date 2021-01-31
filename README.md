# aws-ecs-exercise

## Task

Configuring an end to end deployment pipeline on AWS that manages the lifecycle
of a web application.

## Tech Stack

- `flask`: Flask is a popular, extensible web microframework for building web
  applications with Python.
  
  Due to its simplicity, I used Flask to develop the
  simple web application. The web application is serving on port 5000 and it
  justs prints a hello message to the page.

- `GitHub Actions`: GitHub Actions can orchestrate any workflow, based on any
  event, while GitHub manages the execution, provides rich feedback, and secures
  every step along the way.

  When looking for an easy way to deploy onto ECS, I saw a workflow online which
  was maintained by `aws-actions` and decided to use it for my CI/CD pipeline

- `Amazon CodeBuild`: AWS CodeBuild is a fully managed continuous integration
  service that compiles source code, runs tests, and produces software packages
  that are ready to deploy.

  In my setup, I used CodeBuild as an environment for executing my dummy unit
  test. Depending of the status of the tests, by using webhooks, codebuild can
  report the status of the tests back to GitHub.

- `Amazon ECS`: Amazon Elastic Container Service (Amazon ECS) is a fully managed
  container orchestration service that makes it easy to operate containerized
  workloads at scale.  It also integrates with other core AWS services, such as
  Amazon Route 53, AWS Identity and Access Management (IAM), and Amazon
  CloudWatch.  Establishing an effective and efficient CI/CD pipeline is
  critical for containerized applications, regardless of the platform you are
  using to manage your containers.

  Since it was included in the free-tier, I used it in my stack.

- `Amazon ECR`: Amazon Elastic Container Registry (ECR) is a fully managed
  container registry that makes it easy to store, manage, share, and deploy your
  container images and artifacts anywhere.

  Since it was included in the free-tier, I used it in my stack.

- `AWS Fargate`: AWS Fargate is a serverless compute engine for containers that
  works with both Amazon Elastic Container Service (ECS) and Amazon Elastic
  Kubernetes Service (EKS). Fargate makes it easy for you to focus on building
  your applications. Fargate removes the need to provision and manage servers,
  lets you specify and pay for resources per application, and improves security
  through application isolation by design.

  Since I did not want to build manage and maintain servers and resources for
  this simple webapp and due to my interest in serverless computing, I used it.

- `AWS Command Line Interface`: The AWS Command Line Interface (CLI) is a
  unified tool to manage your AWS services. With just one tool to download and
  configure, you can control multiple AWS services from the command line and
  automate them through scripts.

- `AWS Cloud Development Kit`: The AWS Cloud Development Kit (AWS CDK) is an
  open source software development framework to define your cloud application
  resources using familiar programming languages. I used the python wrapper of
  AWS CDK for defining, deploying and destroying my infrastructure.

### Deploying the Infrastructure

```bash
cd ecs-devops-sandbox-cdk
cdk init --language python 
# Activate your Python virtual environment
source .env/bin/activate
# Install CDK Python general dependencies
pip install -r requirements.txt
# Install CDK Python ECS dependencies
pip install aws_cdk.aws_ec2 aws_cdk.aws_ecs aws_cdk.aws_ecr aws_cdk.aws_iam aws_cdk.aws-ecs-patterns
cdk deploy
```

### Destroying the Infrastructure

```bash
cd ecs-devops-sandbox-cdk
cdk destroy
```

## Screenshots

### Deploying the infrastructure with aws-cdk

![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/cdk-deploy.png)
### Triggering Amazon CodeBuild with a commit
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/git-sha.png)
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/code-build.png)

### Building and pushing the current webapp to ECR

![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/ecr-repositories.png)

#### Applying the task definition
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/github-actions-successful-pipeline.png)
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/checks.png)

#### The old version and new version deployed with GitOps
![pic](https://github.com/dgokcin/aws-ecs-exercise/blob/master/pic/gitops.png)

The deployed service can be accessed from the
[DNS](http://ecs-d-ecsde-18m8t9v4jik0t-167631541.eu-west-2.elb.amazonaws.com)
name of the loadbalancer.

### References

- [AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
- [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)
- [AWS CDK Installation](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
