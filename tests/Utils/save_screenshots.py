class SaveScreenshots:
    @staticmethod
    def save_screenshot(driver,path_base,us_id):
        driver.save_screenshot(f"{path_base}{us_id}.png")
