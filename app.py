#!/usr/bin/env python3

print( "Hi" )


class ConvolutionNeuron:
    
    def __init__( self ):
        self.weight = 0
        self.bias   = 0

    def forward( self, X ):
        return X * self.weight + self.bias

    def __call__( self, X ):
        return self.forward( X )
