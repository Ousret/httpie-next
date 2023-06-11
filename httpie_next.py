"""
Use (unofficial-experimental) urllib3[h2n3] alongside HTTPie.
"""
import json
import os.path
from os import makedirs

from httpie.plugins import TransportPlugin
from httpie.config import DEFAULT_CONFIG_DIR
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager

import typing


__version__ = '1.0.0'
__author__ = 'Ahmed TAHRI'
__licence__ = 'MIT'


class QuicCapabilityCache(
    typing.MutableMapping[typing.Tuple[str, int], typing.Optional[typing.Tuple[str, int]]]
):

    def __init__(self):
        self._cache = dict()
        if not os.path.exists(DEFAULT_CONFIG_DIR):
            makedirs(DEFAULT_CONFIG_DIR, exist_ok=True)
        if os.path.exists(os.path.join(DEFAULT_CONFIG_DIR, "httpie.quic.json")):
            with open(os.path.join(DEFAULT_CONFIG_DIR, "httpie.quic.json"), "r") as fp:
                self._cache = json.load(fp)

    def save(self):
        with open(os.path.join(DEFAULT_CONFIG_DIR, "httpie.quic.json"), "w+") as fp:
            json.dump(self._cache, fp)

    def __contains__(self, item: typing.Tuple[str, int]):
        return f"QUIC_{item[0]}_{item[1]}" in self._cache

    def __setitem__(self, key: typing.Tuple[str, int], value: typing.Optional[typing.Tuple[str, int]]):
        self._cache[f"QUIC_{key[0]}_{key[1]}"] = f"{value[0]}:{value[1]}"
        self.save()

    def __getitem__(self, item: typing.Tuple[str, int]):
        key: str = f"QUIC_{item[0]}_{item[1]}"
        if key in self._cache:
            host, port = self._cache[key].split(":")
            return host, int(port)

        return None

    def __delitem__(self, key: typing.Tuple[str, int]):
        key: str = f"QUIC_{key[0]}_{key[1]}"
        if key in self._cache:
            del self._cache[key]
            self.save()

    def __len__(self):
        return len(self._cache)

    def __iter__(self):
        yield from self._cache.items()


class HTTPAdapterWithQuicCache(HTTPAdapter):

    def __init__(self):
        super().__init__()

        # remove previously created PM (from super call)
        del self.poolmanager

        self.poolmanager = PoolManager(
            preemptive_quic_cache=QuicCapabilityCache(),
            num_pools=self._pool_connections,
            maxsize=self._pool_maxsize,
            block=self._pool_block,
        )


class HTTPNextTransportPlugin(TransportPlugin):

    name = 'urllib3-experimental'
    prefix = "https://"

    def get_adapter(self):
        return HTTPAdapterWithQuicCache()
