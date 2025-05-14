variable "aws_region" {
  description = "The AWS region to deploy into."
  type = string
  default = "us-east-1"
}

variable "project_name" {
  description = "A base name for Project"
  type = string
  default = "tf-ci-cd-demo"
}
variable "ami_id" {
  description = "The ID of the AMI for EC2 instance."
  type = string
  default = "ami-084568db4383264d4"
}

variable "instance_type" {
  description = "The type of EC2 instance to Launch"
  type = string
  default = "t2.micro"
}

variable "key_pair_name" {
  description = "The name of SSH pair to use."
  type = string
  default = "aws-us-east-1-key.pem"
}

variable "security_group_name" {
  description = "The name for the SSH security group"
  type = string
  default = "My-Web_Server-SG"
}

variable "ssh_allowed_cidr" {
  description = "The CIDR block allowed to SSH into the instance."
  type        = string
  default     = "43.243.83.34/32"
}

variable "vpc_id" {
  description = "The ID of the VPC to deploy resources into (optional, defaults to default VPC if empty)"
  type        = string
  default     = ""
}
