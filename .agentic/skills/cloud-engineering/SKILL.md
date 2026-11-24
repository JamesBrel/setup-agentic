# Skill: Cloud Engineering (`cloud-engineering`)

## 1. Purpose
Cloud infrastructure architecture, serverless, container orchestration, and Well-Architected frameworks.

## 2. Activation Conditions
- Designing cloud infrastructure on GCP, AWS, or Azure
- Authoring Terraform / OpenTofu Infrastructure as Code
- Configuring cloud networking, load balancers, and managed databases

## 3. Required Knowledge
- Cloud Well-Architected Framework: Reliability, Security, Cost, Performance, Operations
- Infrastructure as Code (Terraform, CloudFormation) modularization and state management
- Container orchestration (Kubernetes, GCP Cloud Run, AWS ECS)
- Cloud networking: VPC, subnets, NAT gateways, peering, and security groups

## 4. Execution Methodology
- 1. Architecture Topology: Design cloud resource diagram with multi-zone redundancy.
- 2. IaC Definition: Author declarative Terraform modules with explicit variables and outputs.
- 3. Networking & Security: Restrict database subnets to private access; route traffic via API Gateway.
- 4. Observability Integration: Configure centralized cloud logging and metric dashboards.
- 5. Cost Estimation: Calculate monthly infrastructure expenditure using pricing calculators.
- 6. IaC Validation: Execute terraform validate, tflint, and tfsec.

## 5. Best Practices
- Store Terraform remote state in encrypted cloud storage with state locking enabled.
- Never open database ports (5432, 3306) to the public internet (0.0.0.0/0).
- Tag all cloud resources with Project, Environment, and Owner metadata for cost tracking.

## 6. Common Mistakes to Avoid
- Hardcoding cloud credentials in Terraform files or provider blocks.
- Over-provisioning resources resulting in unnecessary cloud expenses.
- Creating single-zone architectures for production workloads.

## 7. Validation Criteria
- terraform validate and tflint pass with 0 errors.
- tfsec / checkov security scan reports zero high-severity misconfigurations.
- Architecture review confirms multi-AZ failover capability.

## 8. Relevant Tools
`Terraform, OpenTofu, tflint, tfsec, Google Cloud SDK, AWS CLI`

## 9. Authoritative References
- Google Cloud Architecture Framework (cloud.google.com/architecture/framework)
- AWS Well-Architected Framework Documentation
