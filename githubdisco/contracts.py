from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail
from json import loads

class WithMetaContract(Contract):
    """
    Merges a dict into the response.meta dict
    @with_meta { "foo": "bar" }
    """

    name = 'with_meta'

    def adjust_request_args(self, args):
        meta = args.get('meta', {})
        meta = meta if meta is not None else {} # meta could be already set as None, explicitly
        meta.update(loads(' '.join(self.args)))
        args['meta'] = meta
        return args
