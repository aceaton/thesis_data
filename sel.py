from selenium import webdriver

# Define the list of websites to visit
# websites = [
#     "https://www.example.com",
#     "https://www.google.com",
#     "https://www.openai.com",
# ]

websites = [
    "https://www.google.com"]
# "https://www.Youtube.com"]
# "https://www.Facebook.com"]
# "https://www.Baidu.com"]
# "https://www.Wikipedia.org"]
# "https://www.Qq.com"]
# "https://www.Taobao.com"]
# "https://www.Tmall.com"]
# "https://www.Yahoo.com"]
# "https://www.Amazon.com"]

# Initialize the web driver (you'll need to specify the path to your driver)
driver = webdriver.Chrome(executable_path="/Users/annaeaton/Downloads/chromedriver-mac-x64-119/chromedriver")

try:
    # Loop through the list of websites
    for website in websites:
        print(f"Accessing {website}...")
        
        # Navigate to the website
        driver.get(website)
        
        # You can add any actions or interactions you want here
        
        # Print the title of the page
        print("Title:", driver.title)
        
        # Print the URL
        print("URL:", driver.current_url)
        
        # Wait for a few seconds (you can customize this)
        driver.implicitly_wait(7)
        
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Close the web driver when done
    driver.quit()
