resource "aws_iam_policy" "Route53UpdaterPolicy" {
  name = "route53updater-Route53UpdaterPolicy"
  path = "/"
  policy = jsonencode(
    {
      Statement = [
        {
          Action = [
            "route53:ChangeResourceRecordSets",
            "route53:ListResourceRecordSets",
          ]
          Effect   = "Allow"
          Resource = "*"
        },
        {
          Action = [
            "route53:ListHostedZonesByName",
          ]
          Effect   = "Allow"
          Resource = "*"
        },
      ]
      Version = "2012-10-17"
    }
  )
}
