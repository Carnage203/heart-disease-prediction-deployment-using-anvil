from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def CHECK_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    """This method is called when the button is clicked"""
    Heart_Disease=anvil.server.call('CHECK',
                              self.Age.text,
                              self.Sex.text,
                              self.Chest_pain_type.text,
                              self.BP.text,
                              self.Cholestrol.text,
                              self.FBS_Over_120.text,
                              self.EKG_Results.text,
                              self.Exercise_angina.text,
                              self.ST_depression.text,
                              self.Slope_of_ST.text,
                              self.Number_of_vessels_fluro.text,
                              self.Thallium.text,
                              )
    if Heart_Disease=="true":
      self.Heart_Disease.visible=True
      self.Heart_Disease.text="You have Heart Disease"
    else:
      self.Heart_Disease.visible=True
      self.Heart_Disease.text="You do not have Heart Disease"

    



  

  