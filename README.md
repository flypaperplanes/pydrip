# Python Drip Client

This python drip client is maintained by Matthew Clarkson from [Paper Planes](https://flypaperplanes.co), a data driven digital marketing agency based in Brisbane, Queensland Australia.

## Installation

To install this package run `pip install pydrip`.

## Usage

To use this package, simply import and initialize the DripClient from python-drip as follows:

```python

from pydrip import DripClient

drip = DripClient(token=YOUR_ACCESS_TOKEN, account_id=YOUR_ACCOUNT_ID)

# Get Subscribers
status, data = drip.subscribers()
subscribers = data['subscribers']

# Create a Subscriber
subscriber = {
    'subscribers': {[
        { 'email': 'test@test.com' }
    ]}
}

drip.create_or_update_subscriber(subscriber)

```

About 90% of the API is covered.

## Todo
- Documentation
- Test it ;)

