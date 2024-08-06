---
# Leave the homepage title empty to use the site title
title:
date: 2024-08-04
type: landing

sections:
# Home
  - block: slider
    id: home-section

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

# About

  - block: markdown
    id: about-section
    title: About Us
  - block: hero
    content:
      title: About Us
      image:
        filename: team.jpg  
      text:
         We are an interdisciplinary research group at the interface of genomics, biophysics, and precision medicine. Our mission is to develop new genomic technologies to map and model cellular dysfunction in human disease.

# News
  - block: markdown
    id: news-section
    content:
      title: 
      subtitle:
      text: |
        {{< news_poput >}}
    design:
      view: card
      columns: '1'

# People
  - block: people
    id: people-section
    content:
      title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Members
          - Visitors
          - Alumni
      sort_by: Params.order_pos
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true

  - block: markdown
    content:
      title: ' '
      subtitle: '**Alumni**'
      text: |

          | Name | Position in the lab    | Years | Next Position                 |
          |--------------------|------------|-------|-------------------------------|
          | Emma Walsh | Research Assistant | 2023  | PhD student, Cambridge University |

      design:
          # Choose how many columns the section has. Valid values: '1' or '2'.
          columns: '1'


# Publications and Resources
  - block: markdown
    id: publications-section
    content:
      title: Publications and Resources
      subtitle: ''
      text: |
        {{% publications_resources %}}
      design:
        columns: '1'
        background:
          image: 
            filename: 
            filters:
              brightness: 1
            parallax: false
            position: center
            size: cover
            text_color_light: true
        spacing:
          padding: ['20px', '0', '20px', '0']
        css_class: fullscreen

# Contact
  - block: contact
    features:
      map:
        provider: 'google'
        api_key: ''
        zoom: 15
    content:
      title:
      coordinates:
        latitude: '57.68611268875995'
        longitude: '11.95872255330746'
      text: If you are interested in joining our team, please send us an email. We always welcome application for postdocs, PhD students, research assistants, MsC Students, etc.
      email: joan.camunas@gu.se
      phone:
      address:
        organization:
        street: Dept. Medical Biochemistry & Cell Biology, Medicinaregatan 9C
        city: Gothenburg
        region:
        postcode: '41390'
        country: Sweden
        country_code: SE

      #directions: Enter 9C and go one level up. First glass door on the right as you exit the elevator.
      #office_hours:
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: Twitter
          link: 'https://x.com/JoanCamunas'
      #appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'

      # Automatically link email and phone or display as text?
      autolink: true

      # Email form provider
      #form:
      #  provider: netlify
      #  formspree:
      #    id:
      #  netlify:
          # Enable CAPTCHA challenge to reduce spam?
      #    captcha: false
    design:
      columns: '1'


---
