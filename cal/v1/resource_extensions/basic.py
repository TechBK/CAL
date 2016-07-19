# from openframework.v1.wsgi import Controller


class BasicController(object):

    # Define support for GET on a collection
    def index(self, req):
        data = {
            'action': "index",
            'controller': "basic",
            'cloud': req.environ['cal.cloud']
        }
        return data

    def delete(self, req, id):
        data = {
            'action': "delete",
            'controller': "basic",
            'id': id,
            'cloud': req.environ['cal.cloud']
        }
        return data

    def update(self, req, id):
        data = {
            'action': "update",
            'controller': "basic",
            'id': id,
            'cloud': req.environ['cal.cloud']
        }
        return data

    def create(self, req):
        data = {
            'action': "create",
            'controller': "basic",
            'cloud': req.environ['cal.cloud']
        }
        return data

    def show(self, req, id):
        data = {
            'action': "show",
            'controller': "basic",
            'id': id,
            'cloud': req.environ['cal.cloud']
        }
        return data


    def detail(self, req):
        data = {
            'action': 'detail',
            'controller': 'basic',
            'cloud': req.environ['cal.cloud']
        }
        return data

    def mem_action(self, req, id):
        data = {
            'action': 'mem_action',
            'controller': 'basic',
            'id': id,
            'cloud': req.environ['cal.cloud']
        }
        return data


class Basics:
    collection_name = 'basics'
    member_name = 'basic'
    controller = BasicController()
    parent_resource = {}
    collection = {'detail': 'GET'}
    member = {'mem_action': 'GET'}


    # Defining a method implements the following API responses:
    #   delete -> DELETE
    #   update -> PUT
    #   create -> POST
    #   show -> GET
    # If a method is not definied a request to it will be a 404 response

    # It is also possible to define support for further responses
    # See `servers.py <http://git.openstack.org/cgit/openstack/nova/tree/nova/nova/api/openstack/compute/servers.py>`_.


# class Basic(extensions.V3APIExtensionBase):
#     """Basic Test Extension."""
#
#     name = "BasicTest"
#     alias = ALIAS
#     version = 1
#
#     # Both get_resources and get_controller_extensions must always
#     # be definied by can return an empty array
#     def get_resources(self):
#         resource = extensions.ResourceExtension('test', BasicController())
#         return [resource]
#
#     def get_controller_extensions(self):
#         return []