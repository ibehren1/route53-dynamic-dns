resource "aws_iam_user" "route53updater" {
  name = "route53updater"
  path = "/"
  tags = {}
}

resource "aws_iam_access_key" "route53updater_key" {
  user = aws_iam_user.route53updater.name
}

output "route53updater_access_key" {
  description = "route53 user access_key"
  value       = aws_iam_access_key.route53updater_key.*.id
}
output "route53updater_access_secret" {
  description = "route53 user access_secret"
  value       = aws_iam_access_key.route53updater_key.secret
}

resource "aws_iam_policy_attachment" "policy-attachment" {
  name       = "policy-attachment"
  users      = [aws_iam_user.route53updater.name]
  policy_arn = aws_iam_policy.Route53UpdaterPolicy.arn
}
