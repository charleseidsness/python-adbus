#!/usr/bin/env python3

# Copyright: 2017, Charles Eidsness
# pylint: disable=C0330

"""test of low-level sd-bus wrapper of an exported method"""

import unittest
import asyncio
import adbus

class Test(unittest.TestCase):
    """sd-bus wrapper method test cases"""

    @staticmethod
    def test_method_basic():
        """test a basic method"""

        def _callback(arg1):
            """test callback"""
            print(f"callback {arg1}")
            return True

        loop = asyncio.get_event_loop()

        service = adbus.Service("adbus.test", loop)
        service.add_object("/adbus/test/methods", "adbus.test",
                [adbus.Method("BasicMethod", _callback, arg_signature='a{ii}',
                    return_signature='v')])

        async def run_method():
            """Run the method"""
            for i in range(1, 20):
                print("+"*i)
                await asyncio.sleep(1)
                print("-"*i)
                await asyncio.sleep(1)

        loop.run_until_complete(asyncio.gather(
            run_method(),
            ))
        loop.close()

if __name__ == "__main__":
    unittest.main()
