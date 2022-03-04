from enum import Enum

from selenium.webdriver.common.by import By

class EnumIdentifierType(Enum):
    no_type           = None
    id                = By.ID
    name              = By.NAME
    xpath             = By.XPATH
    tag_name          = By.TAG_NAME
    css_selector      = By.CSS_SELECTOR
    class_name        = By.CLASS_NAME
    partial_link_text = By.PARTIAL_LINK_TEXT