import pygame

class square:
    
    def __init__(this,x,y,width,height):
        #x = hàng, y = cột
        this.x=x
        this.y=y
        #chiều dài chiều rộng
        this.width=width #8
        this.height=height #8
        #luôn dương, tỉ lệ với hàng,cột (8), luôn ở trong cửa sổ game
        this.abs_x=x*width
        this.abs_y=y*height
        #vị trí của các ô vuông
        this.abs_position=(this.abs_x,this.abs_y) 
        this.position=(x,y)
        #bắt đầu tô màu cho ô 
        this.color='light' if(x+y)%2==0 else 'dark'
        this.draw_color=(246,174,45) if this.color =='light' else (51,101,138) 
        #dùng để xác định nước đi hay ăn
        this.highlight_color=(114,155,121) if this.color == 'light' else (196,109,94)
        
        this.fill=None
        this.coord=this.get_coord()
        this.highlight=False
        
        this.rect=this.rect(this.abs_x,this.abs_y,this.width,this.height) #lấy ô vuông
    
    #điền a,b,c,...,h theo x và y trên bàn cờ
    def get_coord(this):
        columns = 'abcdefgh' #các cột
        return columns[this.x] + str(this.y + 1) #nhét vào hàng x tương ứng với cột y+1
    
    def draw(this, display):
        # tô màu cho màu sáng hoặc tối
        if this.highlight:
            pygame.draw.rect(display, this.highlight_color, this.rect)
        else:
            pygame.draw.rect(display, this.draw_color, this.rect)
            
        # thêm icon chess
        if this.occupying_piece != None:
            centering_rect = this.occupying_piece.img.get_rect()
            centering_rect.center = this.rect.center
            display.blit(this.occupying_piece.img, centering_rect.topleft)
        
        

