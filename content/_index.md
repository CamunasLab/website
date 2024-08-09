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
      # Each slide represents a section in the slider
      - title: Investigating cellular heterogeneity in human tissue
        content: # Add additional text content here if needed
        align: center # Alignment of the slide content
        background:
          image:
            filename: islets.jpg # Background image for the slide
            filters:
              brightness: 0.7 # Adjust brightness of the background image
          position: right # Position of the background image
          color: '#666' # Overlay color on the image
      - title: Developing biophysical tools to study cell function
        content: # Add additional text content here if needed
        align: left
        background:
          image:
            filename: cellpick.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: Precision medicine tools to improve human health
        content: # Add additional text content here if needed
        align: right
        background:
          image:
            filename: team.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap # Icon to display on the link
          icon_pack: fas # Icon pack to use
          text: Join Us # Text for the link
          url: ../contact/ # URL the link points to

    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true # Whether the slider should be fullscreen
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 1500

  - block: hero
    id: about-section
    content:
      title: About Us
      image:
        filename: team.jpg
      text: |
        We are an interdisciplinary research group at the interface of genomics, biophysics, and precision medicine. Our mission is to develop new genomic technologies to map and model cellular dysfunction in human disease.
        
    
        
        <a href="../about/" style="
          display: inline-flex;
          align-items: center;
          color: rgba(0, 0, 0, 0.8); /* Ensure text color contrasts with background */
          text-decoration: none; /* Remove underline */
          padding: 0px 15px;
          background-color: rgba(150, 200, 255, 0.5); /* Adjusted to make the link stand out */
          border-radius: 5px;
          transition: background-color 0.3s;
          font-size: 1rem;
          gap: 28px; /* Space between text and icon */
        ">
          Read more about our research
          <i class="fas fa-arrow-right" style="
            color: #4A90E2; /* Icon color */
            font-size: 1.2rem;
          "></i>
        </a>
    link:
      icon: info-circle
      icon_pack: fas
      text: Learn More
      url: ../about/ <!-- Ensure this path matches the actual URL of your About page -->

    design:
      slide_height: ''
      is_fullscreen: true






  # News Section
  - block: markdown
    id: news-section
    content:
      title: # Title for the news section
      subtitle: # Subtitle for the news section
      text: |
        {{< news_poput >}} 
    design:
      view: card # Display style for the news items
      columns: '1' # Number of columns for the news items

  # People Section
  - block: people
    id: people-section
    content:
      title: Meet the Team
      # Choose which groups/teams of users to display.
      # Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
        - Members
        - Visitors
        - Alumni
      sort_by: Params.order_pos
      sort_ascending: true
    design:
      show_interests: false # Whether to show interests of team members
      show_role: true # Whether to show roles of team members
      show_social: true # Whether to show social links of team members

  # Alumni Section
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

  # Publications and Resources Section
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
            filename: # Filename for the background image
            filters:
              brightness: 1 # Adjust brightness of the background image
            parallax: false # Whether the background image should have a parallax effect
            position: center
            size: cover
            text_color_light: true # Whether the text color should be light
        spacing:
          padding: ['20px', '0', '20px', '0'] # Padding for the section
        css_class: fullscreen

  # Contact Section
  - block: contact
    id: contact-section
    features:
      map:
        provider: 'google'
        api_key: '' # Google Maps API key
        zoom: 15 # Zoom level for the map
    content:
      title: Contact # Title for the contact section
      coordinates:
        latitude: '57.68611268875995'
        longitude: '11.95872255330746'
      text: |
        If you are interested in joining our team, please send us an email. We always welcome application for postdocs, PhD students, research assistants, MsC Students, etc.
      email: joan.camunas@gu.se
      phone: # Phone number (if any)
      address:
        organization:
        street: Dept. Medical Biochemistry & Cell Biology, Medicinaregatan 9C
        city: Gothenburg
        region:
        postcode: '41390'
        country: Sweden
        country_code: SE

      # directions: Enter 9C and go one level up. First glass door on the right as you exit the elevator.
      # office_hours: # Office hours (if any)
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: Twitter
          link: 'https://x.com/JoanCamunas'
      # appointment_url: 'https://calendly.com' # URL for scheduling appointments (if any)
      # contact_links:
      #   - icon: comments
      #     icon_pack: fas
      #     name: Discuss on Forum
      #     link: 'https://discourse.gohugo.io'

      # Automatically link email and phone or display as text?
      autolink: true

      # Email form provider
      # form:
      #   provider: netlify
      #   formspree:
      #     id:
      #   netlify:
      #     # Enable CAPTCHA challenge to reduce spam?
      #     captcha: false
    design:
      columns: '1'
---
