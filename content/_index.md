---
# Leave the homepage title empty to use the site title
title:
date: 2024-08-04
type: landing

sections:
  - block: slider
    content:
      slides:
      - title: Investigating cellular heterogeneity in human tissue
        content:
        align: center
        background:
          image:
            filename: islets.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Developing biophysical tools to study cell function
        content:
        align: left
        background:
          image:
            filename: cellpick.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: Precision medicine tools to improve human health
        content:
        align: right
        background:
          image:
            filename: team.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Join Us
          url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 1500

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
