from dataclasses import dataclass


@dataclass
class Person:
  """Class for keeping track of a participant in the Secret Santa."""
  name: str
  email: str
  secret_santa_name: str
  secret_santa_email: str
