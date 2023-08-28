# Generated by Django 3.2.20 on 2023-07-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscriptions", "0001_squashed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="planfeature",
            name="feature_type",
            field=models.CharField(
                choices=[
                    ("cname", "Custom domain"),
                    ("cdn", "CDN public documentation"),
                    ("ssl", "Custom SSL configuration"),
                    ("support", "Support SLA"),
                    ("private_docs", "Private documentation"),
                    ("embed_api", "Embed content via API"),
                    ("search_analytics", "Search analytics"),
                    ("pageviews_analytics", "Pageview analytics"),
                    ("concurrent_builds", "Concurrent builds"),
                    ("sso", "Single sign on (SSO) with Google"),
                    ("urls", "Custom URLs"),
                    ("audit-logs", "Audit logs"),
                    ("audit-pageviews", "Audit logs for every page view"),
                ],
                max_length=32,
                verbose_name="Type",
            ),
        ),
    ]