ec2_info = [
    {
        "name" : "ec2-1",
        "type" : "t2.micro"
    },
    {
        "name" : "ec2-2",
        "type" : "t2.micro"
    },
    {
        "name" : "ec2-3",
        "type" : "t2.micro"
    }
]

# Accessing values
print(ec2_info[0]["name"])  # Output: ec2-1
print(ec2_info[0]["type"])  # Output: t2.micro
# Adding a new key-value pair
ec2_info[0]["ip"] = "1.2.3.5"
print(ec2_info)  # Output: [{'name': 'ec2-1', 'type': 't2.micro', 'ip': '1.2.3.5'}, {'name': 'ec2-2', 'type': 't2.micro'}, {'name': 'ec2-3', 'type': 't2.micro'}]