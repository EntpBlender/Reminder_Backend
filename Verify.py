import requests
def ValidateEmail(EmailRecipient):
  response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params = {'email': EmailRecipient})

  status = response.json()['status']
  if status == "valid":
  #  print("email is valid")
    EmailValid = True
  elif status == "invalid":
    print("email is invalid")
    EmailValid = False
  else:
    print("email was unknown")
    EmailValid = False

  return EmailValid


if __name__ == "__main__":
  print("no")
  exit
