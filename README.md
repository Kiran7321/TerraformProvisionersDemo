# Deploying a flask app that shows top 25 animes using Terraform Provisioners

→ using provisioners we can make terraform to make things on resources

→ for e.g., we can use it to deploy an app on the ec2 instance that is created using terraform

→ resource creation/destruction along with performing required actions within

→ if there’s no provisioner concept, we might have to use shell script / ansible to connect these resources after they’re created and then we can perform the actions we want

→ so that’s why terraform introduced provisioners [ local exec, remote exec, file ]

→ **remote exce** provisoner let us do this and **local exec** let us format the terraform o/p that we get on the shell when we run the terraform commands. 

→ because if we’re createing large infra then when we run **apply** we see lot of info on the shell right which would be hard to follow. If we can just save it a file, it would be easy to audit. 

→ **file provisioner** is to copy files to resources that terraform will create

→ all the code is commented for understandability and you must have an idea of how to deply manually then only, you can understand how to automate using Terraform

→ full tutorial available  [here](https://www.youtube.com/watch?v=dX-sbUs9Sk0&list=PLdpzxOOAlwvI0O4PeKVV1-yJoX2AqIWuf&index=15)

→ **app.py**
![Screenshot 2024-09-18 at 1 31 21 PM](https://github.com/user-attachments/assets/7caf5cd8-bb4f-40aa-8037-44eac55d9220)
→ **deployment**
![Screenshot 2024-09-18 at 1 32 03 PM](https://github.com/user-attachments/assets/e03fe5c4-38ec-48b3-a816-3366ebad7ba8)
→ **destruction** 
![Screenshot 2024-09-18 at 1 35 07 PM](https://github.com/user-attachments/assets/79739970-7fcf-4069-ad4d-cf4765cc4b84)
![Screenshot 2024-09-18 at 1 34 58 PM](https://github.com/user-attachments/assets/a9456731-b5b3-49db-913a-b13631f396b8)


