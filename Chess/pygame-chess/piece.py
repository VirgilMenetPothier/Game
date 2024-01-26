import os
import pygame
# used to get the sprites from the picture "pieces.png"
class Piece(pygame.sprite.Sprite):
    def __init__(self, filename, cols, rows):
        pygame.sprite.Sprite.__init__(self)
        self.pieces = {
            "white_pawn":   0,
            "white_knight": 1,
            "white_bishop": 2,
            "white_rook":   3,
            "white_king":   4,
            "white_queen":  5,
            "black_pawn":   6,
            "black_knight": 7,
            "black_bishop": 8,
            "black_rook":   9,
            "black_king":   10,
            "black_queen":  11
        }
        self.spritesheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.cell_count = cols * rows

        #to get the dimensions of the picure
            #self.rect = self.spritesheet.get_rect()
            #w = self.cell_width = self.rect.width // self.cols
            #h = self.cell_height = self.rect.height // self.rows
        w = 500 // self.cols
        h = 167 // self.rows
        #get the with and height of a cell, to get each pieces picture

        self.cells = list([(i % cols * w, i // cols * h, w, h) for i in range(self.cell_count)])
        #put in a list the position of each cells
    def draw(self, surface, piece_name, coords):
        piece_index = self.pieces[piece_name]
        surface.blit(self.spritesheet, coords, self.cells[piece_index])

