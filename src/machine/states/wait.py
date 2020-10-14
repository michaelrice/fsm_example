import asyncio

from machine.states.base import BaseState
from machine.states.exit import Exit
from machine.api import wsclient


class Wait(BaseState):
    def on_event(self):
        print("Waiting")
        # implement some kind of
        # waiting logic
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            wsclient.wait_for_update(
                token="8WMlMtAxZnifhVqnsUnM2M8nB6OTQHmR0lwxUnJ2OjHqI5Lu--xkrkSoN32JLI_lBnQg_MRv8Y3DqsLU4di36nobNklaLuy5Hvk3eW4m74Rdk39nLSE6YpuD-YXDREV8EdxhdNx2-fip0C0ilHPS2_PQWqRn9OIjxMKlmWQFo7qfPHxg8QJxtOR50jzSbSyTPooVv4uMbkRd5r-6e0M5YiRRZAA_m3vmq8mEZf8APVv9_hLZaPR1NAnPZ4TgcmysFTVDMCbFjHv43LeS7nhzFtyz3gelITp-0I8xefOAO8rDWCNwMoU-4DulgMrbxEsmSvOwV6t54mPPrsQihum-0kUR50k34yQmtK4mYWVKXmCfs1mJWGY9WxxEcAonKXJ-LWEjByjXJuPJEqFflOrmtmkajBNJ98qHBPNQyJaNL32pyYNFMpolHuV5FJHg0TBXPU99ZQ70W16PHncESc2Tg1tAE_rwhwE9qDUDt7lc8dmWPqELhQ71x53kkhy1rPZuQGVQyfeX6H0GW0ZpY9qALhzZHjCicXcAC5zZTaViT9CdybK9za0UKJDu5Jnr2Sa8cmJf9STKXOjtSSaKRrkFkdbwTZJVhEBxd0RVj2RFg2VUCQXj8uZrChC9ziq88ps3MR61rKHNaVcSEZJIgXwwOcXeJBlIhQbF7W_a1XR1C-_rFtdwwRdytFiymNZAe-7x33BY_ibeAvSjD6Shorz4bSWLA_mTsVjjWeOgSpQNX0klAkZHzbo04jIYUFm2jzMiKUdk0U6xaxYjOHMfz4DJ9ywDamrlqUchOJMRfR6jClzwAbcYNY7BmxYC9eZ9t_-1Y-382ci82sEfOvW3RUVK-R8654p7bcQalp5HOuV9cV-OGa63F9_LvQE=",
                uri="https://drp.mrice.internal:8092/api/v3",
                machine="4f35c80a-cba2-4a09-9215-2fbb0ba0d0fb"
            )
        )
        print("got machine event. leaving wait for exit.")
        return Exit()

