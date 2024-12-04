import behave_webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Set Chrome options for headless execution in CI environments
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")

    try:
        # Initialize the behave WebDriver with Chrome options
        context.behave_driver = behave_webdriver.Chrome(options=options)
        context.behave_driver.set_page_load_timeout(30)  # Set timeout for page loads
        context.behave_driver.implicitly_wait(10)        # Set implicit wait timeout
    except Exception as e:
        print(f"Failed to initialize WebDriver: {e}")
        raise

def after_all(context):
    # Safeguard against accessing an uninitialized driver
    if hasattr(context, "behave_driver") and context.behave_driver:
        try:
            context.behave_driver.quit()
        except Exception as e:
            print(f"Error while quitting WebDriver: {e}")