from db import Model, engine
import models

Model.metadata.drop_all(engine)
