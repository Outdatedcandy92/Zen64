
## What am I making?

I'm making a super minimalist 75% wireless mechanical keyboard that has a sliding potentiometer on the side for volume control.

### Time Spent Overall: 14 Hours

# June 30th - PCB Finished

I started off with the schematic, I made a 5 row and 16 col matrix array (I got rid of the function keys). 
Since I wanted this project to be super minimal and wireless I went with the nice! nano v2 as my board, it has a nrf chip and support for battery charging on board which made it a perfect choice. It however did not have enough gpio pins for the matrix. To fix this I simply used a MCP I2C IO expander chip, I decided to go with the SOP package for it as I will most likely be hand soldering it later.
Adding a sliding potentiometer in my keyboard  was a bit difficult as it was very tough to find footprint and a CAD for them. I scoured on aliexpress and found a listen that had some product dimension sketches in its description. I used those dimesions to reverse engineer a 3D model and a footprint, I decided to add a 0.2mm tolerance on the holes for the footprint just in case.

*Product Dimension Sketch*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/d06701cef173bc851c394f43430b69feec25a2c2_image.png)

*3D Model I designed based of the sketch*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/18cffbd3cf11651713cd99af4ba2992f05bf3351_image.png)

After making the footprint and a 3D model for the potentiometer I started working on my schematics, it was a pretty easy task and took like 10 minutes.

*Keyboard Schematics*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/8ca960dca27e2647a227c675267b3d7ae8d76a00_image.png)



Now making the PCB was a bit more time consuming that the schematic as I had to first assign footprints to all the components and then manually align each and every key in the matrix. I routed all my keys in the matrix first, decided to keep all the column traces on one side and row traces on another to make sure I don't need any vias. After that I routed everything to the IO expander, It took about 3 revisions of routing to get it perfect and the end result was a beautifully routed PCB ;).
 
*The PCB*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3472ff2942c0b3540b1ecaa5aa97e079d6f14de6_image.png)


![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/761f250cfe56b3a2e4c188f8988a74cfe7c764a3_image.png)


### Time Spent: 6 Hours

# July 1 - Finished It!!

I made some minor improvements to the PCB such as adding led status indicators and a connector for the battery. Plus added some mounting holes onto the board too.

*Updated Schematics*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/672afb1c8a07e3fb32834377ed7b4427ceb5dd40_image.png)
*Updated PCB*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/917677c9ef9b898c5b560c11c6122953b7485d8b_image.png)


After finishing this I exported the PCB as a step file and imported it into fusion 360, I also generated a plate dxf file for this keyboard and imported it into fusion. Since I was going for a super minimal design I just decided to keep it simple and elegant, just a simple case with a fillet on the bottom, sort of how my keychron looks. I did choose not to add any incline in my case and instead have holes on the bottom which I could press fit angled feet into.

*Overall Keyboard Design*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ae0a91df372773982591f5da0041ae73c9f6c988_image.png)

*Back Side*
![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ae0a91df372773982591f5da0041ae73c9f6c988_image.png)


*Detachable 10 degree incline feet*

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/d951b5a0b717ba0267ce7b1ae1e1f64e416df64a_image.png)


*Inside the case*

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/330af171066aa2bd7bbae44d0c58a470cb32ddd0_image.png)


*Keyboard Render (looks heat)*

![img](https://hc-cdn.hel1.your-objectstorage.com/s/v3/792f07ad1e167e6d8d1c609f7a2cfceaba23b083_image.png)



After finishing up my case I went on to create a BOM for this project, all of my parts are sourced from aliexpress as its the cheapest option for me and I find it quite reliable. I've decided to use cherrymx reds for this project as I need it to be quiet. for modifications I left like a 6mm gap between the pcb bottom and case bottom, and I'm going to be filling it up with 3mm EVA foam and then 2mm soft silicon foam layered on top of it. Overall my BOM comes up to about $150 USD for this project.

I also created a github repo and exported all my project and production files and added them to the repo.


### Time Spent: 8 Hours

