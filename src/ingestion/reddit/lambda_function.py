import praw

def lambda_handler(event, context):
    return {"statusCode": 200, "body": f"Deployment verified: {context.function_name} is live!"}