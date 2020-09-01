# SFIA Project 2 – Email Generator

# Table of Contents

_**[SFIA Project 2 – Email Generator 1](#_Toc49834192)**_

**[Resources 1](#_Toc49834193)**

**[Requirements 1](#_Toc49834194)**

**[Risk Assessment 2](#_Toc49834195)**

**[Project Tracking 3](#_Toc49834196)**

**[Current Release 1.1 3](#_Toc49834197)**

[User Interface 5](#_Toc49834198)

[Next Release Version 1.2 5](#_Toc49834199)

**[CI Pipeline 5](#_Toc49834200)**

[Configure 7](#_Toc49834201)

[Testing 8](#_Toc49834202)

[Build 8](#_Toc49834203)

[Deploy 8](#_Toc49834204)

**[Author 9](#_Toc49834205)**

**[Contributors 9](#_Toc49834206)**

**[Acknowledgements 9](#_Toc49834207)**

## Resources

GIT: [Repo](https://github.com/jcbgrub/SFIA_Project_2)

The App: [Here](http://34.105.174.30/)

Kanban Board: [JIRA](https://jacobhpgrub.atlassian.net/jira/software/projects/SP2/boards/5)

Presentation: [Google-Slides](https://docs.google.com/presentation/d/12cQJEWHPvVS07wNUDt_qEfelDd0V2vmVwS70mfTqgfQ/edit)

## Requirements

The requirements of this project is to create an app based on a service-orientated architecture application, this application must be composed of at least 4 services that work together. The key requirements of the project are as follows:

- An Asana board with full expansion on tasks needed to complete the project.
- Risk Assessment
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

## Risk Assessment

The risk assessment produced for the project can be found below. It attempts to cover all risks or threats involved and what would be done to eliminate or reduce the impact of these threats.

| Type | Assessment | Risk | Impact | Responsibility | Response | Tolerance |
| --- | --- | --- | --- | --- | --- | --- |
| HTTP traffic attack | Connecting to Googles VM are not secure. Any data transferred could be read by outsiders | medium | high | Jacob grub | In this could we would need to take the website offline and make an overall root and user password reset | Treat |
| DB attacked | Attacks can bypass security when data is committed to the DB | low | medium | Jacob Grub | Close the DB and inform users that data has been breached and drop and recreate the DB | Tolerate |
| Downtime between updates | When a new release goes online the website is temporarily not reachable | high | low | Jacob Grub | To avoid this we are using an orchestration tool, Swarm allows us to cluster Docker containers on different nodes so if one webserver crashes there are others to shoulder the load. | Tolerate |
| SQL crashes | If the cloud host goes down access to the database would fail and the website could not be accessed | low | low | Google Cloud Platform | Switch to a different cloud provided while contacting GCP. | Tolerable |
| Web server crashes | If the virtual machine on which the app runs goes down the website could crash | low | high | Jacob Grub | To avoid this we are using an orchestration tool, Swarm allows us to cluster Docker containers on different nodes so if one webserver crashes there are others to shoulder the load. | Treat |
| API exceeding limit request | If multiple users try to access the website it could be overloaded | high | high | Jacob Grub | In order to avoid this we use Nginx web server as a load balancer to equalise traffic to different mashines | Treat |

## Project Tracking

Jira was the chosen method when planning the project and tracking the progress  **and to satisfy the brief.**  This increment (release version 1.1) has been set to be delivered within 1 standard length sprint of 2 weeks starting on the 18/8/20 to be completed on the 1/9/20 the delivery date for the first increment and project deadline. **Story points are set by 1h=1point.**

The current sprint named **Release 1.1,** contains one epic which represent this release. These then are split in individual user stories focused on Configuration (the CI Pipeline), backend (services, routes), front end (HTML) functionality, testing and documentation. Each user story has several children which represent the smaller steps which needed to be completed.

This release all user stories have been completed apart from the user story Troubleshooting which deals with current bugs and errors in the application.

![Screenshot 2020-09-01 at 05 26 44](https://user-images.githubusercontent.com/45181318/91799607-4d1b5680-ec1f-11ea-954b-8c9db3e442ad.png)

## Current Release 1.1

At this point there has been 1 release and 1 pre-release of the app. Release 1.1 was released on the 28th of August and satisfies MVP (Minimum Viable Product).

![Screenshot 2020-09-01 at 06 51 00](https://user-images.githubusercontent.com/45181318/91799698-80f67c00-ec1f-11ea-98f5-98a39b407e30.png)


To satisfy the requirements I developed a simple app which generates a random email. **Following the**  **service-orientated architecture application requirement,** the app is split into 4 services as the below diagram illustrates.

**Service1**

- User makes a request through a Jinja2 based template. Service1 sends a GET request to service 2 and 3.
- Response 2 and 3 are concatenated and a POST request send to Service4.
- Reponse4 is committed to an SQL based Database.
- Uses port 5000

**Service2**

- Generates a random name &#39;object&#39;, that is
- Uses port 5001

**Service3**

- Generates a random number &#39;object&#39;.
- Uses port 5002

**Service4**

- Receives the email name and concatenates an email domain based on the attributes of that object.
- Uses port 5003

![Screenshot 2020-09-01 at 06 51 33](https://user-images.githubusercontent.com/45181318/91799730-953a7900-ec1f-11ea-80c6-9fb085dcf8fb.png)

### User Interface

In its current version the user uses a two-step approach when using the website. The user will land on the _Generate_ page which offers the possibility to generate a random email address by clicking a link (frigure1).

![Screenshot 2020-09-01 at 06 52 00](https://user-images.githubusercontent.com/45181318/91799763-a4b9c200-ec1f-11ea-8401-6b62458d8048.png)

Afterwards the user can go to the _All Email_ page were a list of generated emails is found while the idem with last ID.

![Screenshot 2020-09-01 at 06 52 29](https://user-images.githubusercontent.com/45181318/91799803-b602ce80-ec1f-11ea-9eef-d4c1683e2659.png)

### Next Release Version 1.2

There are a number of improvements which will be included in the new

1. User Experience: Some of the content should be phrased in a more comprehensible way.
2. The generate page at this moment does not show the generated email, the user has to pick up the generated email from the DB list on the home page.

## CI Pipeline

The entire app is built and maintained using a Jenkins based CI Pipeline. As below figure1 illustrates. The source code Is based on **Python** and pushed/pulled to **Version Control Git** based on the user stories pushed/pulled from **JIRA.**

![CI_Pipeline](https://user-images.githubusercontent.com/45181318/91799906-ea768a80-ec1f-11ea-87d1-3dcd15ed6045.png)

Every push triggers the **Webhook** to Jenkins, is an open source automation server, which helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery.
# 1
 Our Jenkins Pipeline is based on four stages: **Configure, Test, Build and Deploy (firgure2).**

![Screenshot 2020-09-01 at 06 54 29](https://user-images.githubusercontent.com/45181318/91799932-fd895a80-ec1f-11ea-9c73-d120f1cfea0f.png)

### Configure

This is the first step in the Pipeline. Ansible is an open-source software provisioning, configuration management, and application-deployment tool. Ansible will reach out to the virtual machines (VM) from Google Cloud Platform (GCP) and configure the three main VMS by:

1. Setting up SSH Protocols meaning the seamless connection and communication between virtual machines.
2. Initiating and joining Docker Swarm.

Swarm mode for Docker is a container orchestration tool exists natively for Docker, meaning that there are no other installation requirements other than Docker. As an orchestration tool, Swarm allows us to cluster Docker containers on different nodes for redundancy and high availability, meaning we can have containers deployed over multiple virtual machines.

For our purposes there is one Manager (sfia-manager) and two Workers (sfia-worker-1 and sfia-worker-2).

![Screenshot 2020-09-01 at 06 54 49](https://user-images.githubusercontent.com/45181318/91799962-0aa64980-ec20-11ea-8165-c2a718aa6bfb.png)


### Testing

The second stage is testing. The main tool used for unit testing is **Pytest**. All services but servie1 have a 100% coverage. While servie1 has 97%. This percentual difference is due to the fact that I did not test to commits to the database. This could have been integrated but during the setup of the services framework I manually verified that all data is committed to the database. Below are the test reports.

![Screenshot 2020-09-01 at 06 55 38](https://user-images.githubusercontent.com/45181318/91800015-27428180-ec20-11ea-97e0-69eb1d2d49a2.png)

### Build

The next step in the pipeline builds containers using Docker. Compose for Docker is a tool that allows you to define and run multiple Docker containers with a command by using a single configuration file. **So in our build we are creating a container for each service and pushing it to Docker hub.** This is down with the help of a **Dockerfile,** a YAML based configuration file for each service.

### Deploy

The last step in the Pipeline, which pulls the latest version of our containers from Docker hub to get deployed to a live environment. Docker stack was used when in the manager node that allows for the management of a cluster of docker containers with the use of the docker swarm initiated in the configure stage. This docker stack used the images previously pushed to the chosen docker hub repository.

##

## Author

Jacob Grub

## Contributors

Thanks to Luke Benson and Harry Volker for their excellent mentoring.

Thanks to A. for her

## Acknowledgements

Thanks to QA Consulting for their expertise.

[1](#sdfootnote1anc) https://en.wikipedia.org/wiki/Jenkins\_(software)
