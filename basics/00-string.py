# single quote

MyVar='AWS'
print(MyVar)

# double quote
my_var="Terraform"
print(my_var)

# triple quote  
stack_list = '''
    Linux
    Git
    Ansible
    Terraform
    Docker
    Kubernetes
    Python
'''
print(stack_list)
# formate
message=f"DevOps-tools are {stack_list} and cloud-{MyVar}"
print(message)

# capitalize
name="royal"
print(name.capitalize())

# uppercase
name="royal"
print(name.upper())

# lowercase
name="ROYAL"
print(name.lower())

# starts with
instance_id = "i-1234567890abcdef0"
print(instance_id.startswith("i-"))

# endswith
instance_id = "vol-0123456789abcdef0"
print(instance_id.startswith("i-"))

# join
name = "royal reddy"
updated_name = "-".join(name)
print(updated_name)

# split
my_list = name.split(" ")
print(my_list)

# split with separator
my_list = updated_name.split("-")
print(my_list)

# partition  
information = "I am a DevOps Engineer"
print(information.partition("DevOps"))
