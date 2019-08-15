# xkcd comics post generator for vk.com

This program downloads random comics from [xkcd.com](https://xkcd.com) and uploads it to your group on [vk.com](vk.com).

### How to install

Log into your [vk.com](https://vk.com) account.
Create an application with standalone type on [vk.com](https://vk.com/dev), go to "My Apps"/"Create application".
Get `client_id` for your app: click "Manage"/"Settings". Place it into .env file using this form: `XKCD_CLIENT_ID=7090448`
Get access token, using [Implicit Flow](https://vk.com/dev/implicit_flow_user) procedure. It is easy, your request should looks like this: [https://oauth.vk.com/authorize?client_id=7090448&display=page&scope=photos,groups,wall,offline&response_type=token&v=5.101&state=123456](https://oauth.vk.com/authorize?client_id=7090448&display=page&scope=photos,groups,wall,offline&response_type=token&v=5.101&state=123456). Replace with your `client_id` and `v` - actual vk api version (if nessessary). Copy link to your browser.

On the new screen the application will ask access to your groups, wall etc, so click OK. You'll get a new link in your browser with access token in it. It looks like this: [https://oauth.vk.com/blank.html#access_token=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef&expires_in=0&user_id=246785&state=123456](https://oauth.vk.com/blank.html#access_token=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef&expires_in=0&user_id=246785&state=123456). Place token into your .env file using this form: `VK_IMPLICIT_FLOW_TOKEN=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef`.

Get group_id of your vk group. Use this service for it: [http://regvk.com/id/](http://regvk.com/id/). Copy your group link here and you'll get the group id number. Place it into .env file using this form: `XKCD_GROUP_ID=-195514543`. Note the minus sign this is part of the form!

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

`$ python3 main.py`

A new post will be created on your vk group.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).