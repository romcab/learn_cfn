from troposphere import Template, apigateway, Ref


def write_to_file(filename:str, data:str):
    with open(filename, 'w') as out:
        out.write(data)

template = Template()

template.set_description("JR-API gateway")

api = template.add_resource(apigateway.RestApi(
    "API",
    Description="Job Registry API via CloudFormation",
    Name="CF-Rom-Job Registry API",
    EndpointConfiguration=apigateway.EndpointConfiguration(Types=["REGIONAL"])
))

api_image_method = template.add_resource(apigateway.Method("auth",
    ResourceId="auth",
    ApiKeyRequired=False,
    AuthorizationType="NONE",
    HttpMethod="PUT",
    RestApiId=Ref(api),
    Integration=apigateway.Integration(
        Uri="",
        IntegrationResponses=[
            apigateway.IntegrationResponse(
                "Default",
                StatusCode="200",
            ),
            apigateway.IntegrationResponse(
                "Error",
                StatusCode="400",
            )
        ],
        PassthroughBehavior="when_no_match",
        IntegrationHttpMethod="POST",
        ContentHandling="CONVERT_TO_TEXT",
        Type="AWS"
    ),
    MethodResponses=[
        apigateway.MethodResponse("Success",
            StatusCode="200",
        ),
        apigateway.MethodResponse(
            "Error",
            StatusCode="400"
        )
    ]
))

print(template.to_json())
write_to_file("templates/jr-api.yaml", template.to_yaml(clean_up=True))


