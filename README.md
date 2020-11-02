# Monitoring User Activity Period Over a Month Online
This Project aims at maintaining the data base for user activity period,that is the time when a particular user started the session and when that particular session gets over and along with that, it fetches all the data for activity periods and deliver it to the user online as the user only needs to hit the url.
This project is hosted on the publicly accessible cloud Heroku, so user can easily access and see the activity period of particular users in real time over all duration.
# Requirements to Run the Application on Localhost
<b> Dependencies </b>

Project requires:

- Python (>= 3.6)
- Django (>= 3.0)

<b> Repository Cloning Using Gitbash </b>

To fetch the source code from the git to your local machine,we need to run the below mentioned command git bash


```
git clone https://github.com/sammortals/FullThrottleAssignment.git
```

<b> Packages Installation </b>

If you already have a working installation of numpy and pandas, the easiest way to install the required packages,is using `pip`

```
pip install -r requirements.txt
```

<b> Command to Run the Application on LocalHost Server </b>

Run the below mentioned command from your python terminal and your server will be open on localhost with port 8000

```
python assignment\manage.py runserver
```

# REST API
API Endpoint is hosted on Heroku Server, So you can hit our published API endpointson Postman to consume the API at your end.

The REST API to the example APP of user activity period is described below

## Step to Consume APIs on Postman

### Request
Enter the below url by selcting method = GET in postman tab
```
GET http://localhost:8080/
```
### Response
 The below response is of json type
```
{
    "ok": "true",
    "members": [
        {
            "id": "1",
            "real_name": "sameer",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "2020-10-24T20:44:01.873938Z",
                    "end_time": "2020-10-24T21:01:49.210017Z"
                },
                {
                    "start_time": "2020-10-24T21:09:22.247201Z",
                    "end_time": "2020-10-24T21:09:27.730550Z"
                },
                {
                    "start_time": "2020-10-24T21:09:46.519321Z",
                    "end_time": "2020-10-24T21:09:49.581942Z"
                }
            ]
        },
        {
            "id": "2",
            "real_name": "amit",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "2020-10-24T21:09:04.548885Z",
                    "end_time": "2020-10-24T21:09:10.225383Z"
                },
                {
                    "start_time": "2020-10-24T21:09:34.968815Z",
                    "end_time": "2020-10-24T21:09:38.052566Z"
                }
            ]
        }
    ]
}
```
