# Creating model architecture.
# from hate.entity.config_entity import ModelTrainerConfig
# from keras.models import Sequential
# from keras.optimizers import RMSprop
# from keras.callbacks import EarlyStopping, ModelCheckpoint
# from keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D
# from hate.constants import *

from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.layers import LSTM, Dense, Embedding, SpatialDropout1D
from hate.constants import *

class ModelArchitecture:

    def __init__(self):
        pass

    
    def get_model(self):
        # model = Sequential()
        # model.add(Embedding(MAX_WORDS, 100,input_length=MAX_LEN))
        # model.add(SpatialDropout1D(0.2))
        # model.add(LSTM(100,dropout=0.2,recurrent_dropout=0.2))
        # model.add(Dense(1,activation=ACTIVATION))
        # model.summary()
        # model.compile(loss=LOSS,optimizer=RMSprop(),metrics=METRICS)

        # return model

        model = Sequential()

            # Embedding layer
        model.add(Embedding(
            input_dim=MAX_WORDS,
            output_dim=100,
            # Removed input_length as it's deprecated
            input_length=MAX_LEN,
            mask_zero=False  # Better handling of variable length sequences
        ))
        
        # Dropout layer for embeddings
        model.add(SpatialDropout1D(0.2))
        
        # LSTM layer
        model.add(LSTM(
            units=100,
            dropout=0.2,
            recurrent_dropout=0.2
        ))
        
        # Output layer
        model.add(Dense(1, activation=ACTIVATION))

        model.build(input_shape=(None, MAX_LEN))
    
        
        # Compile the model
        model.compile(
            loss=LOSS,
            optimizer=RMSprop(),
            metrics=METRICS
        )
        
        # Display model summary
        model.summary()
        
        return model