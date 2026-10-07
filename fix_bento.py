import re

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-bento-grid.liquid', 'r') as f:
    content = f.read()

# Add illustrations before <div class="bento-action-footer">
illustrations = {
    'One-Cable Docks': '''
        <div class="bento-illustration-container">
          <div class="bento-visual-dock">
            <div class="bento-dock-box">
              <span class="dock-light-glow"></span>
              <div class="dock-port-strip">
                <span class="mini-port usb-c"></span>
                <span class="mini-port usb-a"></span>
                <span class="mini-port aux"></span>
              </div>
            </div>
          </div>
        </div>
        <div class="bento-action-footer">''',
    'Extra Wide Desk Screens': '''
        <div class="bento-illustration-container">
          <div class="bento-visual-monitor">
            <div class="mini-monitor-frame">
              <div class="mini-monitor-screen">
                <div class="mini-bar top"></div>
                <div class="mini-card-grid">
                  <div class="mini-card"></div>
                  <div class="mini-card"></div>
                </div>
              </div>
            </div>
            <div class="mini-monitor-stand"></div>
          </div>
        </div>
        <div class="bento-action-footer">''',
    'Adjustable Laptop Stands': '''
        <div class="bento-illustration-container">
          <div class="mini-stand-frame">
            <div class="mini-stand-laptop-holder"></div>
            <div class="mini-stand-base"></div>
          </div>
        </div>
        <div class="bento-action-footer">''',
    'Comfortable Wireless Mice': '''
        <div class="bento-illustration-container">
          <div class="mini-mouse-body">
            <div class="mini-mouse-wheel"></div>
          </div>
        </div>
        <div class="bento-action-footer">''',
    'Quiet &amp; Comfortable Keyboards': '''
        <div class="bento-illustration-container">
          <div class="mini-keyboard-plate">
            <div class="mini-key-row">
              <span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
            <div class="mini-key-row">
              <span></span><span></span><span></span><span></span><span></span><span></span>
            </div>
            <div class="mini-key-row space">
              <span class="spacebar"></span>
            </div>
          </div>
        </div>
        <div class="bento-action-footer">'''
}

blocks = content.split('<div class="bento-card-wrapper')
new_content = [blocks[0]]

for block in blocks[1:]:
    for key, ill in illustrations.items():
        if key in block:
            block = block.replace('<div class="bento-action-footer">', ill)
    new_content.append('<div class="bento-card-wrapper' + block)

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-bento-grid.liquid', 'w') as f:
    f.write("".join(new_content))
