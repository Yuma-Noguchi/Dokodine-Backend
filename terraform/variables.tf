variable "project_id" {
  description = "The ID of the Google Cloud project"
}

variable "region" {
  description = "The region to deploy the Cloud Run service"
}

variable "service_name" {
  description = "The name of the Cloud Run service"
}

variable "repository_id" {
  description = "The ID of the Artifact Registry repository"
}

variable "organization" {
  description = "The ID of the Google Cloud organization"
}

variable "workspace" {
  description = "The name of the Terraform Cloud workspace"
}