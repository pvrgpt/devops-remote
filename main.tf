# main.tf

# Configure the AWS Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# --- Resources ---

# Create a Security Group allowing SSH access
resource "aws_security_group" "ssh_sg" {
  name        = var.security_group_name
  description = "Allow SSH inbound traffic"
  vpc_id      = var.vpc_id # You'll need a VPC ID or let it default to the default VPC

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_allowed_cidr] # Be specific with your IP in production!
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All protocols
    cidr_blocks = ["0.0.0.0/0"] # Allow all outbound traffic
  }

  tags = {
    Name = "${var.security_group_name}-sg"
  }
}

# Launch an EC2 instance
resource "aws_instance" "web_server" {
  ami           = var.ami_id         # Get a valid AMI ID for your region and desired OS
  instance_type = var.instance_type
  key_name      = var.key_pair_name  # Associate the key pair
  vpc_security_group_ids = [aws_security_group.ssh_sg.id] # Associate the security group

  tags = {
    Name = "${var.project_name}-webserver"
  }
}

# --- Outputs ---

# Output the public IP of the EC2 instance
output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web_server.public_ip
}

# Output the public DNS of the EC2 instance
output "instance_public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.web_server.public_dns
}
