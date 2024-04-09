# AWS Cloud Adoption Assistance Using LLMs

## Context

The past decade has witnessed a phenomenal rise in cloud computing adoption. From a nascent technology in the
early 2010s, cloud services have become an indispensable part of modern IT infrastructure. This surge can be
attributed to several factors. Firstly, the entry of tech giants like Amazon, Microsoft, and Google into the
cloud arena with robust offerings like AWS, Azure, and Google Cloud Platform (GCP) made these services accessible
to a wider audience. Synergy Research Group reports that cloud service spending grew at a staggering 56%
annually from 2009 to 2019, dwarfing the 4% average annual growth seen in data center spending during the same
period. Secondly, the scalability and cost-effectiveness of cloud solutions proved highly attractive to
businesses of all sizes. Companies no longer needed hefty upfront investments in hardware and software,
and could now pay only for the resources they utilized. Finally, advancements in security protocols and
compliance certifications addressed initial concerns about data privacy in the cloud, paving the way for wider
enterprise adoption.

Amazon Web Services (AWS), a pioneer in the cloud market, exemplifies this growth trajectory. Over the years,
AWS has relentlessly expanded its service portfolio, encompassing everything from storage (S3) and compute (EC2)
to databases (RDS) and artificial intelligence (SageMaker). This comprehensive suite caters to diverse business
needs and fosters a dynamic cloud ecosystem.

<img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb384f75-2fbb-4c5b-9d5e-b97557d02f33_1572x1894.png" alt="AWS resources expansion" width="500" style="display: block; margin: 0 auto"/>

## Problem

However, the very features that fuel AWS's dominance – it's expansive service portfolio and unmatched
scalability – also introduce a new hurdle for cloud adopters. While the initial surge in cloud computing
was driven by the convenience and cost-effectiveness of these services, as exemplified by AWS's growth,
navigating the intricacies of this vast ecosystem presents a significant learning curve. Unlike traditional
on-premise IT environments with a limited set of tools, AWS offers hundreds of services, each with its own
functionalities, pricing models, and use cases. Mastering this complex landscape requires a deep understanding
of individual services, their potential trade-offs, and the intricate ways they can be interconnected.
Building a truly scalable, reliable, and efficient system on AWS demands the ability to orchestrate these
services in a cohesive manner.

For instance, choosing between Amazon S3 and EBS for storage depends on factors
like access frequency, data persistence needs, and cost optimization. Similarly, integrating services like an
Amazon Relational Database Service (RDS) instance with an Auto Scaling group for web applications necessitates
an understanding of their interaction patterns and potential bottlenecks. This knowledge gap can be a hurdle
for organizations transitioning to the cloud, potentially leading to suboptimal deployments or unforeseen costs.

## Proposed Solution

One potential solution to bridge the knowledge gap and streamline AWS adoption is the utilization of Large
Language Models (LLMs). These AI models, trained on vast amounts of data, can be leveraged to generate initial
AWS system design alternatives based on a high-level service description. The LLM would analyze the use case,
identify relevant AWS services, and propose a preliminary architecture. This initial design could then be
further refined through a series of follow-up questions posed to the LLM. These questions could delve into
specific requirements like scalability needs, cost constraints, and security considerations. By iteratively
refining the service selection and configuration based on the LLM's responses, users can arrive at a more
optimized AWS architecture. This LLM-driven approach could significantly reduce the time and expertise needed
to navigate the complex AWS service landscape.

Furthermore, the generated design could be directly translated into a Cloud Development Kit (CDK) template
by another LLM specializing in code generation. This would automate the infrastructure provisioning process,
ensuring consistency and reducing the risk of human error. By leveraging the combined power of these LLMs,
organizations can streamline their cloud adoption journey and build secure, scalable, and cost-effective AWS solutions.

## General Goal

**To develop a cloud adoption assistance system that leverages Large Language Models (LLMs) to automate AWS system design
and infrastructure provisioning based on high-level service description**

## Specific Goals

* **Define the project requirements from a brief high level description and some follow up questions**
  * Modify [GPTPilot](https://github.com/Pythagora-io/gpt-pilot) to refine the requirements and create artifacts,
  like user stories and use cases.
* **Use a Large Language Model conversational agent to create a low level AWS architecture design using the requirements as input**
  * Fine tune a open source LLM like [Llama 2](https://llama.meta.com/) to convert requirements into architecture
* **Use a Large Language Model code agent to create a CDK template using the low lever architecture as input**
  * Fine tune a open source LLM like [Llama 2](https://llama.meta.com/) to convert architecture into CDK