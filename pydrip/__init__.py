import requests
import json


class TokenNotFoundException(Exception):
    pass


class AccountIDNotFound(Exception):
    pass


class DripClient(object):
    """Python 3 Drip Client.
    
    This is the a Python 3 client for the Drip API.
    It is maintained by Matthew Clarkson from https://flypaperplanes.co
    """
    
    def __init__(self, **kwrds):

        self.headers = {}

        if not 'token' in kwrds.keys():
            raise TokenNotFoundException('Please provide an access token.')

        if not 'account_id' in kwrds.keys():
            raise AccountIDNotFound('Please provide an account ID')

        if 'application_name' in kwrds.keys():
            self.headers['User-Agent'] = kwrds['application_name']

        self.token = kwrds['token']
        self.account_id = kwrds['account_id']
        self.api_url = 'https://api.getdrip.com/v2'
        self.auth = requests.auth.HTTPBasicAuth(self.token, '')

    def _get(self, path, arguments=None):
        url = '%s/%s/%s' % (self.api_url, self.account_id, path)
        response = requests.get(url, headers=self.headers, auth=self.auth, params=arguments)
        return (response.status_code, response.json())
    
    def _post(self, path, payload):
        url = '%s/%s/%s' % (self.api_url, self.account_id, path)
        response = requests.post(url, headers=self.headers, json=payload, auth=self.auth)
        return (response.status_code, response.json())

    def _delete(self, path):
        url = '%s/%s/%s' % (self.api_url, self.account_id, path)
        response = requests.delete(url, headers=self.headers, auth=self.auth)
        return (response.status_code, response.json())

    ### ACCOUNTS ###

    def accounts(self):
        url = '%s/accounts' % (self.api_url,)
        response = requests.get(url, headers=self.headers, auth=self.auth)
        return (response.status_code, response.json())

    def account(self, account_id):
        """Fetch an account."""
        url = '%s/%s' % (self.api_url, self.account_id)
        response = requests.get(url, headers=self.headers, auth=self.auth)
        return (response.status_code, response.json())
 
    ### BROADCASTS ###

    def broadcasts(self, arguments=None):
        """List all broadcasts."""
        return self._get('broadcasts', arguments)

    def broadcast(self, broadcast_id):
        """Fetch a broadcast."""
        path = 'broadcasts/%s' % (broadcast_id,)
        return self._get(path)

    ### BROADCASTS ###

    def campaigns(self, arguments=None):
        """List all campaigns."""
        return self._get('campaigns', arguments)
 
    def campaign(self, campaign_id):
        """Fetch a campaign."""
        path = 'campaigns/%s' % (campaign_id,)
        return self._get(path)

    def activate_campaign(self, campaign_id):
        """Activate a campaign."""
        path = 'campaigns/%s/activate' % (campaign_id,)
        return self._post(path, campaign_id)

    def pause_campaign(self, campaign_id):
        """Pause a campaign."""
        path = 'campaigns/%s/pause' % (campaign_id,)
        return self._post(path, campaign_id)

    def campaign_subscribers(self, campaign_id):
        """List subscribers to a campaign."""
        path = 'campaigns/%s/subscribers' % (campaign_id,)
        return self._get(path, campaign_id)

    def subscribe(self, campaign_id, payload):
        """Subscribe someone to a campaign."""
        path = 'campaigns/%s/subscribers' % (campaign_id,)
        return self._post(path, payload)
    
    def campaign_subscriptions(self, subscriber_id):
        """List all campaign subscriptions for a subscriber."""
        path = 'subscribers/%s/campaign_subscription' % (subscriber_id, )
        return self._get(path)

    ### Custom Fields###

    def custom_fields(self):
        """List all custom field identifiers used in an account"""
        return self._get('custom_field_identifiers')
    
    ### Conversions ###

    def goals(self, arguments=None):
        """List all conversions."""
        return self._get('goals')

    def goal(self, goal_id):
        """Fetch a conversion."""
        path = 'goals/%s' % (goal_id,)
        return self._get(path)

    ### Events ###

    def create_event(self, payload):
        """Create an event."""
        return self._post('events', payload)

    def create_events(self, payload):
        """Create events as a batch."""
        return self._post('events/batches', payload)
    
    def event_actions(self, arguments=None):
        """List all custom events actions used in an account."""
        return self._get('event_actions', arguments)
    
    ### Forms ###
    
    def form(self, form_id):
        """List all forms."""
        path = 'forms/%s' % (form_id,)
        return self._get(path)

    def forms(self, arguments=None):
        """Fetch a form."""
        return self._get('forms', arguments)

    ### Orders ###
    
    def create_orders(self, payload):
        """Create orders in a batch."""
        return self._post('orders/batches', payload)

    def create_or_update_order(self, payload):
        """Create or update an order."""
        return self._post('orders', payload)

    def create_or_update_refund(self, payload):
        """Create or update a refund."""
        return self._post('refunds', payload)

    ### Shopper Acvitity###

    def create_or_update_shopper_cart(self, payload):
        """Create or update a shopper's cart."""
        return self._post('shopper_activity/cart', payload)

    def create_or_update_shopper_order(self, payload):
        """Create or update a shopper activity order."""
        return self._post('shopper_activity/order', payload)

    ### Subscribers ###

    def create_or_update_subscriber(self, payload):
        """Create or update a subscriber."""
        return self._post('subscribers', payload)
       
    def create_or_update_subscribers(self, payload):
        """Create or update a batch of subscriber."""
        return self._post('/subscribers/batches', payload)
    
    def subscribers(self, arguments=None):
        """List subscribers."""
        return self._get('subscribers', arguments)

    def subscriber(self, subscriber_id):
        """Fetch a subscriber."""
        path = 'subscribers/%s' % (subscriber_id,)
        return self._get(path)

    def delete_subscriber(self, subscriber_id):
        """Delete a subscriber."""
        path = 'subscribers/%s' % (subscriber_id,)
        return self._delete(path)

    ## Tags ##

    def tags(self):
        """List all tags used in an account"""
        return self._get('tags')

    def tag(self, payload):
        """Tag a subscriber."""
        return self._post('tags', payload)

    def untag(self, email, tag):
        """Tag a subscriber."""
        path = 'subscribers/%s/tags/%s' % (email, tag)
        return self._delete(path)

    ## Webhooks
    def webhooks(self, arguments=None):
        """List webhooks."""
        return self._get('webhooks', arguments)
    
    def delete_webook(self, webhook_id):
        path = 'webhooks/%s' % (webhook_id,)
        return self._delete(path)


