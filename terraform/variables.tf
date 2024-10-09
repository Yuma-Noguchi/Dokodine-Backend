variable "project_id" {
  description = "The ID of the Google Cloud project"
  default = "dokodine"
}

variable "region" {
  description = "The region to deploy the Cloud Run service"
  default = "europe-west1"
}

variable "service_name" {
  description = "The name of the Cloud Run service"
  default = "dokodine-backend"
}

variable "repository_id" {
  description = "The ID of the Artifact Registry repository"
  default = "dokodine-backend"
}