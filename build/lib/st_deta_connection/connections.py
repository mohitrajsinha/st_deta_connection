from streamlit.connections import BaseConnection
from deta import Deta
from streamlit.runtime.caching import cache_data
import pandas as pd
import streamlit as st

class DetaBaseConnection(BaseConnection[Deta]):
    def _connect(self, **kwargs) -> Deta:
        """
        Connect to the Deta Base using the provided project_key.

        Args:
            **kwargs: Additional keyword arguments passed to the connection.

        Returns:
            Deta: An instance of the Deta class representing the Deta Base.
        """
        if '_project_key' in kwargs:
            project_key = kwargs.pop('_project_key')
        else:
            project_key = kwargs['project_key']

        # Connect to Deta Base
        deta = Deta(project_key=project_key)
        return deta

    def fetch(self, collection_name: str, query: dict, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        """
        Fetch data from the Deta Base collection and cache it for the specified time.

        Args:
            collection_name (str): Name of the collection to fetch data from.
            query (dict): Query to filter the data from the collection.
            ttl (int, optional): Time to live (in seconds) for the cached data. Defaults to 3600 seconds (1 hour).
            **kwargs: Additional keyword arguments passed to the fetch function.

        Returns:
            pd.DataFrame: A DataFrame containing the fetched data.
        """
        @st.cache_data(ttl=ttl)
        def _query(collection_name: str, query: dict, **kwargs) -> pd.DataFrame:
            db = self._instance
            collection = db.Base(collection_name)
            response = collection.fetch(query)
            data = list(response.items)  # Convert FetchResponse to a list of items
            return pd.DataFrame(data)

        return _query(collection_name, query, **kwargs)
