import cadquery as cq

PCB = (
       cq.importers.importStep("../DodoKeyboard.step")
         .rotateAboutCenter((0,1,0), 45)
)

show_object(PCB)