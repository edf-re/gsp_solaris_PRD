# Solaris

## Change History
2021.07.26 - Initial release

## Overview:
### Push a button, get an optimized solar project  
The reason for Solaris is to enable Project Developers and Originators to get the most competitive project configuration with the lowest possible LCOE in real-time. The hope is that this leads to a competitive advantage such that EDF constructs an additional 150 MW project per year. This translates into ___$37.5M___ per year in value by assuming EDF realizes approximatley $75M NPV at CoD and assuming the Digital organization gets half the credit for the project being built.

This comes from the Development business setting the 2021 strategy in January:
![GSP Priorities](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/Strat2021.PNG?token=ADPV3PC6FFB74Y6ESJA7SXLBBFD62)

## Objectives:
- Lead to an extra 150 MW solar project per year.
- Get an optimized solar project configuration in real-time.
- The optimization process will be accurate to within $0.50 of the full V&A proforma modeling.
- Improve transparency and coordination between development and SMEs 
- Level up less experienced developers by giving them a window into the drivers behind a bid price.
- Reduce SME workload.

## Success Metrics:
### Value Stream Mapping
![Current Costing Process](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/ValueStreamMapping.png?token=ADPV3PDIY6K5LWQ3W66R3QTBBFLPI)

### Happiness
- Goal: For users (developers and originators) to feel like the platform is giving them a reliable answer, faster.
- Signals: A satisfaction rating from a survey.
- Metrics: Net Promoter Score, satisfaction, can you live without the product?

### Engagement
- Goal: Maximize the number of project configurations considered by a developer.
- Signals: Number of configurations generated for a project. 
- Metrics: Count of `analysis_ids`, average count per project, rate at which new projects are created. 

### Adoption 
- Goal: For all of development to use the platform for solar project development.
- Signals: Number of developers and originators within GSP activly using the platform on a daily basis.
- Metrics: Percent of Development and Origination as daily active users. 

### Retention
- Goal: For GSP development users to rely on the product for thier daily work.
- Signals: Number of repeat users within GSP Development.
- Metrics: Repeat users, daily users, amount of time between user sessions.

### Task Success
- Goal: For users to get an accurate predicted revenue stream. 
- Signals: The number of successful analyses performed on a project.
- Metrics: Analysis count, analyses per week per project. 

## Release Plan
- Q2 2021 - BoP Modeling ([Computron](computron.edfr.com))  
- Q3 2021 - Proforma  
    - Forward price curve inputs
    - PPA revenue modeling
    - Frontend
    - CapEx and OpEx
    - EBITA
- Q4 2021 - Solar Engineering and EPE
    - Layout
    - EPE
    - Construction quanitites - Schedule of Values (SoV)

## Personas
### Project Developer Dominique (PRIMARY)
![Dominique](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/Persona%20-%20Dominique.png?token=ADPV3PA7ULK5ULZGO7JH7MTBBFDW4) 
Dominique joined EDF a year ago right after earning a Master's in Environmental Studies from Yale. Previously, she was a project management intern at the Environmental Defence Fund. She’s quickly becoming familiar with the renewable energy industry and motivated to make a positive impact on the planet via solar development. 

Much of Dominique's job is in the context of project management and so she thinks in terms of construction management and waterfall vs agile practices. She also travels a lot for her job and she can be out of the office up to 75% of the time, visiting sites, meeting with communitees and land owners, or traveling to our corporate headquaters in San Diego. 

Outside of the office Dominique is an outdoor enthusiast. She enjoys canoeing in the Boundary Waters Wilderness, spending time with her community at the local bars, taking her dog to the park, and traveling for vacation.

### Originator Oscar
![Oscar](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/Persona%20-%20Oscar.png?token=ADPV3PH6GEXB6AW6I3EXYWDBBFDYW) 
Oscar has been with EDF for a year. Previously, he was in Oil and Gas so he’s very familiar with mature energy industries. Oscar is the go-to person to ask about business development strategy and market insights. He has an MBA from Northwestern University with a concentration in Finance.

Outside of the office, Oscar is a social foodie. He spent his early childhood in Argentina and loves Burmese food. On the weekends he is often volunteering at Habitat for Humanity, the San Diego Food Bank, or the Star of Hope Mission.

## User Scenarios
Its a Friday in late summer and Dominique has a weekend canoeing trip planned with her community of friends. Its about 8:45 am and she's just arrived at the office. She puts her bag down at her desk and heads toward the kitchen for her first cup of coffee. She's really looking forward to leaving the office a bit early to head out on her trip this afternoon. 

As Dominique checks her phone she sees a last-minute announcement for an RFP due on Monday. "Why do utilities do this to us?", she exclaims as she's heading back to her desk. A difficult part of this job is managing the uncertainty around high-priority, short-deadline delivery dates. Thankfully, she has access to Solaris. 

Within an hour Dominique has pulled up three relevant projects. She's grab the latest, most optimal iteration of each, knowing that Solaris can instantly refresh all the relative aspects of the project and then optimize the configuration at the push of a button. Dominique used to have to worry about the solar technology roadmap getting updated or forward-price curves changes but now those changes are automatically pushed to her phone in real-time. She no longer has to worry about having to coordinate across eight different groups to get the current project assumptions for pricing committee approval. 

Within two hours, Dominique has pricing committee approval to submit the three projects to the RFP, which she can easily do today before heading out on her trip as planned. Each project was considered and ultimately approved using a centralized dashboard that automatically serves up the latest projcet details without having to manually populate a deck. There was one project that was a bit under the hurdle rate but the region has a strategy in place where Dominique six levers that can be affected. Only three of those improvements or mitigations have to be successful within the next six months for the project to work. 

As Dominique wraps up the RFP application she's just in time to head out at 3 pm for the three hour ride to the trip put-in. She won't worry about the RFP or the accuracy of the project modeling as she paddles with her friends and drinks around a campfire that evening. 

## Requirements (Features In)
- Results delivered within minutes.
- Easily accessed via a phone or tablet or laptop
- Seamless pipeline from GIS to V&A processes to get UIRR
    - EPE
    - CapEx
    - OpEx
    - Proforma

## Features Out
- Tax equity
- IRR (including levered returns and outside investment)
- Storage
- Prospecting (modeling across multiple sites)
- Competitor analysis (modeling non-EDF sites)
- SME tools (providing frontends for Technical Services users)
- GIS analysis

## Designs
![Project first design](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/Prelim%20Design%201.png?token=ADPV3PA7B5SUD5NYBXPHXTDBBFD2E)  
![Services first design](https://raw.githubusercontent.com/edf-re/gsp_solaris_PRD/main/Visuals/Prelim%20Design%202.png?token=ADPV3PETBUPB7YVMD3MBQMLBBFD3I)

## Open Issues
- Do we have the right slice?
![What is an MVP?](https://www.spaceo.ca/wp-content/uploads/2020/12/minimum-viable-product-mvp.jpg)

## Q&A
__What is the difference between Solaris, Centralized Assumptions Database, and the Costing Database?__ 

Firstly, Solaris is the platform upon which EDF can build the capability to optimize projects using the computational power of the cloud. This means that within minutes, Solaris can model 10,000 different project scenarios and configurations to show you the 5 most competitive versions to bid into an RFP. It is easliy accessible on your phone or tablet so that you have all the most recent assumptions, inforamtion and project details in real-time.

Solaris is powered by the Centralized Assumptions Database. All the most recent, project-agnostic information and current market assumptions developed by Technical Services are uploaded to the Centralized Assumptions Database. Those assumptions are then automatically ingested into Solaris so that you no longer have to worry about an update to the solar-module roadmap or a forward price curve change. Solaris also uses the same processes as the Costing Database so that you know there won't be any surprises when you go to PFM and V&A for Pricing Committee on Friday.

## Other considerations
None at this time. 