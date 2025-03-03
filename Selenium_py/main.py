import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

if __name__ == "__main__":
    pass 

css_selector = "span.mdc-text-field__ripple"
print(site.get_element_property("css", css_selector, "height"))

xpath = '//*[@id="login"]/div[3]/button/div'
print(site.get_element_property("xpath", xpath, "color"))