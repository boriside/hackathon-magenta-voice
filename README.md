# Skill virtual-teacher

Magenta smart speaker skill to Operate Virtual Teacher App. More info about the app could be found here : [Virtual Teacher](https://remote-rhapsody-platform.hubraum.com/#/projects/5fbbd28663da71001b1d3f83)

## Short Demo of the App [Watch Video](https://www.youtube.com/watch?v=mXDeAB8i0bo)

## Link to virtual room: https://e0b0f2b17d3241528274d533c1f16418.eu-west-1.sumerian.aws/?

## Currently supported dialog:

* Eltern/Kind: Hallo Magenta, starte Lehrer!
* V Lehrer sagt: Hallo … was möchtest du heute machen? Algebra oder Geometrie? Ich kann dir auch einige Fitness Übungen zeigen.
* Kind sagt: Algebra!
* V Lehrer sagt: Was ist die Summe von 3 und 1?
* Kind sagt: 4!
* V Lehrer sagt: Sehr gut. Dann habe ich andere Frage: Wie viel macht es wenn man 3 von 7 subtrahiert?
* Kind sagt: 2!
* V Lehrer sagt: Das stimmt leider nicht so ganz. Lass uns mal wieder probieren Wie viel macht es wenn man 3 von 7 subtrahiert?
* Kind sagt: 4!
* V Lehrer sagt: Sehr gut. Dann habe ich andere Frage: Wie viel macht es wenn man 12 von 34 subtrahiert?
* Kind sagt: Wechseln!
* V Lehrer sagt: Was ist diese Figur? (quadrat, dreieck, kreis, rechteck)
* Kind sagt: Dreieck!
* V Lehrer sagt: Sehr gut. Dann habe ich andere Frage: Was ist das für eine Figur?
* Eltern/Kind: Spiel beenden!

## Services architecture:
![alt text](https://github.com/boriside/hackathon-magenta-voice/blob/main/infrastructure.jpg?raw=true)  

## Pre requisite to integrate Magenta Speaker with VR room (future work):

User needs to register himself before using the APP. Its a One time process when user procures a new speaker. Registration is done following three simple steps

1) Create an account in the Virtual Teacher Portal
2) Register the Magenta speaker there
3) A User Profile will be linked to a URL for the VR room.

## Current Limitaion - Scope for Future work
Portal and user registration feature is not developed as part of the Hackathon. Hence, only one virtual room exists and only a single user can use it at a time currently. This limitation will be addressed once user registration functionality is developed. Please contact us if you notice undesired behaviour of the Virtual Teacher - the reason might be that we are testing simultaneously or we need to clean up the backend.

[![Watch the video](https://res.cloudinary.com/ideation/image/upload/w_1920,c_fit,q_auto,f_auto,dpr_auto/ouqmyj3oy5klffsshhzr)](https://www.youtube.com/watch?v=mXDeAB8i0bo)

## App is making use of these repositories:
- [Virtual Teacher Web](https://github.com/ssharma555/virtual-teacher-web)
- [Virtual Teacher API](https://github.com/ssharma555/virtual-teacher-api) 

