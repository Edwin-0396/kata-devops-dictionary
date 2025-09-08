terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.29.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Namespace
resource "kubernetes_namespace" "dev" {
  metadata {
    name = "dev"
  }
}

# Service account for kata-dictionary
resource "kubernetes_service_account" "kata" {
  metadata {
    name      = "kata-dictionary"
    namespace = kubernetes_namespace.dev.metadata[0].name
  }
}
