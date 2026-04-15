import io
import pandas as pd
import streamlit as st
from sites.sdk.sites import Site, Authenticator

def get_string(space, name, token):
    site = Site(space=space, name=name)
    authenticator = Authenticator.from_token(token)
    content_manager = site.get_content_manager(authenticator=authenticator)
    s = content_manager.download('summary.csv')
    return pd.read_csv(io.StringIO(s.decode()))

st.title("Experiment progress")
space = st.secrets.sites.space
name = st.secrets.sites.name
token = st.secrets.sites.token
st.write(f'loading summary from {space}/{name}...')
df = get_string(space, name, token)
st.write('Done!')
st.write(df)
