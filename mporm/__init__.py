from mporm.oper import Operator
from mporm.schema import Schema
from mporm.model import Model
from mporm.expr import Expr
from mporm.fields import *


class DSN:

    def __init__(self,
                 user,
                 password,
                 database="test", host="localhost", port: int = 3306, charset="utf8"):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.charset = charset
