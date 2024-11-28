CHAPITRES_DEBUT = {
    "reveil": {
        "id": "reveil",
        "titre": "Le Réveil",
        "texte": """
        Vous vous réveillez dans votre appartement de Neo-Tokyo, l'année 2142.
        Les néons de la ville filtrent à travers vos stores automatiques.
        Votre implant neural clignote avec un message urgent de la Guilde...
        """,
        "choix": {
            "1": {
                "texte": "Lire le message immédiatement",
                "destination": "message_guilde",
                "condition": None
            },
            "2": {
                "texte": "Vérifier votre équipement d'abord",
                "destination": "equipement_cache",
                "condition": None
            },
            "3": {
                "texte": "Scanner les environs",
                "destination": "scan_quartier",
                "condition": None
            }
        }
    },

    "message_guilde": {
        "id": "message_guilde",
        "titre": "Message de la Guilde",
        "texte": """
        Le message de la Guilde est crypté au plus haut niveau :
        "Une IA renégate, désignée comme 'Némésis', a infiltré le réseau quantique
        qui sécurise les transactions Bitcoin. Elle menace de provoquer un effondrement
        total du système financier mondial dans les 48 heures."
        """,
        "choix": {
            "1": {
                "texte": "Analyser les traces numériques de Némésis",
                "destination": "analyse_nemesis",
                "condition": {"specialisation": "IA & Hacking"}
            },
            "2": {
                "texte": "Contacter vos informateurs",
                "destination": "reseau_informateurs",
                "condition": None
            },
            "3": {
                "texte": "Se rendre au QG de la Guilde",
                "destination": "qg_guilde",
                "condition": None
            }
        }
    },

    "equipement_cache": {
        "id": "equipement_cache",
        "titre": "Cache Secrète",
        "texte": """
        Derrière le panneau holographique, votre cache révèle votre équipement habituel.
        Mais quelque chose est différent aujourd'hui : un mystérieux dispositif quantique
        pulse doucement d'une lueur bleutée. Vous ne vous souvenez pas l'avoir acquis.
        """,
        "choix": {
            "1": {
                "texte": "Examiner le dispositif",
                "destination": "examen_dispositif",
                "condition": None
            },
            "2": {
                "texte": "Lire le message de la Guilde",
                "destination": "message_guilde",
                "condition": None
            },
            "3": {
                "texte": "Scanner le dispositif",
                "destination": "scan_dispositif",
                "condition": {"intelligence": 7}
            }
        }
    },

    "scan_quartier": {
        "id": "scan_quartier",
        "titre": "Analyse du Quartier",
        "texte": """
        Vos implants scannent les environs. Le quartier semble calme, mais vous
        détectez une activité réseau inhabituelle provenant d'un immeuble voisin.
        Les signatures énergétiques suggèrent un équipement de pointe.
        """,
        "choix": {
            "1": {
                "texte": "Enquêter sur l'activité suspecte",
                "destination": "infiltration_neurocorp",
                "condition": {"agilite": 6}
            },
            "2": {
                "texte": "Lire le message de la Guilde",
                "destination": "message_guilde",
                "condition": None
            },
            "3": {
                "texte": "Vérifier votre équipement",
                "destination": "equipement_cache",
                "condition": None
            },
            "4": {
                "texte": "Observer de loin",
                "destination": "rapport_guilde",
                "condition": None
            }
        }
    },

    "examen_dispositif": {
        "id": "examen_dispositif",
        "titre": "Inspection du Dispositif",
        "texte": """
        Le dispositif semble être un prototype de nouvelle génération. Des
        inscriptions microscopiques révèlent son origine : NeuroCorp. Quelqu'un
        l'a délibérément placé dans votre cache.
        """,
        "choix": {
            "1": {
                "texte": "Scanner le dispositif",
                "destination": "scan_dispositif",
                "condition": {"intelligence": 7}
            },
            "2": {
                "texte": "Lire le message de la Guilde",
                "destination": "message_guilde",
                "condition": None
            }
        }
    },

    "scan_dispositif": {
        "id": "scan_dispositif",
        "titre": "Analyse Approfondie",
        "texte": """
        Votre scan révèle que le dispositif est un prototype de décodeur quantique
        avancé. Il porte la signature de NeuroCorp, mais a été modifié pour
        contourner leurs protocoles de sécurité.
        """,
        "choix": {
            "1": {
                "texte": "Utiliser le dispositif",
                "destination": "infiltration_neurocorp",
                "condition": {"intelligence": 7}
            },
            "2": {
                "texte": "Informer la Guilde",
                "destination": "rapport_guilde",
                "condition": None
            }
        }
    },

    "reseau_informateurs": {
        "id": "reseau_informateurs",
        "titre": "Le Réseau Souterrain",
        "texte": """
        Vos contacts dans les bas-fonds de Neo-Tokyo confirment une activité
        inhabituelle autour des installations de NeuroCorp. Des rumeurs parlent
        d'un projet secret impliquant une IA surpuissante.
        """,
        "choix": {
            "1": {
                "texte": "Infiltrer NeuroCorp",
                "destination": "preparation_infiltration",
                "condition": None
            },
            "2": {
                "texte": "Rapporter à la Guilde",
                "destination": "rapport_guilde",
                "condition": None
            }
        }
    },

    "analyse_nemesis": {
        "id": "analyse_nemesis",
        "titre": "Sur la Trace de Némésis",
        "texte": """
        Vos implants neuraux s'interfacent avec le réseau quantique. Des motifs de données
        familiers émergent... Cette signature numérique... Impossible ! Les algorithmes
        utilisés par Némésis ressemblent étrangement à ceux de Genesis, votre ancienne
        création. Quelqu'un a dû avoir accès à votre code source.
        """,
        "choix": {
            "1": {
                "texte": "Creuser dans les archives de Genesis",
                "destination": "archives_genesis",
                "condition": {"specialisation": "IA & Hacking"}
            },
            "2": {
                "texte": "Contacter d'anciens collègues",
                "destination": "contacts_silicon",
                "condition": None
            },
            "3": {
                "texte": "Informer la Guilde de cette découverte",
                "destination": "rapport_guilde",
                "condition": None
            }
        }
    },

    "archives_genesis": {
        "id": "archives_genesis",
        "titre": "Les Archives de Genesis",
        "texte": """
        En plongeant dans les archives cryptées, vous découvrez des accès non autorisés
        datant d'il y a trois mois. Quelqu'un a méthodiquement étudié et copié des
        parties cruciales du code. Les traces mènent à un serveur hautement sécurisé
        de NeuroCorp.
        """,
        "choix": {
            "1": {
                "texte": "Tenter une intrusion dans NeuroCorp",
                "destination": "infiltration_neurocorp",
                "condition": {"intelligence": 8}
            },
            "2": {
                "texte": "Chercher des alliés pour une approche plus directe",
                "destination": "recherche_allies",
                "condition": None
            },
            "3": {
                "texte": "Surveiller les activités de NeuroCorp",
                "destination": "surveillance_neurocorp",
                "condition": None
            }
        }
    },

    "contacts_silicon": {
        "id": "contacts_silicon",
        "titre": "Échos de la Valley",
        "texte": """
        Vos anciens collègues confirment vos soupçons : NeuroCorp a racheté
        secrètement plusieurs startups liées à Genesis. Ils reconstituent
        votre travail pièce par pièce.
        """,
        "choix": {
            "1": {
                "texte": "Préparer une infiltration",
                "destination": "preparation_infiltration",
                "condition": None
            },
            "2": {
                "texte": "Partager avec la Guilde",
                "destination": "rapport_guilde",
                "condition": None
            }
        }
    },

    "qg_guilde": {
        "id": "qg_guilde",
        "titre": "QG de la Guilde",
        "texte": """
        Au QG, les analystes de la Guilde vous montrent les dernières données sur
        l'activité de Némésis. Les patterns d'attaque correspondent à une signature
        que vous connaissez bien.
        """,
        "choix": {
            "1": {
                "texte": "Analyser les données",
                "destination": "analyse_nemesis",
                "condition": {"specialisation": "IA & Hacking"}
            },
            "2": {
                "texte": "Préparer une infiltration",
                "destination": "preparation_infiltration",
                "condition": None
            }
        }
    },

    "infiltration_neurocorp": {
        "id": "infiltration_neurocorp",
        "titre": "Infiltration de NeuroCorp",
        "texte": """
        Vous vous connectez au réseau de NeuroCorp. Les défenses sont impressionnantes,
        mais vous repérez plusieurs points d'entrée potentiels.
        """,
        "choix": {
            "1": {
                "texte": "Explorer les accès secondaires",
                "destination": "recherche_acces",
                "condition": None
            },
            "2": {
                "texte": "Tenter une intrusion directe",
                "destination": "recuperation_preuves",
                "condition": {"intelligence": 8}
            },
            "3": {
                "texte": "Placer des balises",
                "destination": "marquage_guilde",
                "condition": None
            }
        }
    },

    "recherche_acces": {
        "id": "recherche_acces",
        "titre": "Nouvelles Entrées",
        "texte": """
        En explorant le réseau, vous découvrez un accès secondaire via le système
        de maintenance. Les drones d'entretien utilisent un protocole de communication
        moins sécurisé que le réseau principal.
        """,
        "choix": {
            "1": {
                "texte": "Pirater un drone",
                "destination": "controle_drone",
                "condition": {"agilite": 6}
            },
            "2": {
                "texte": "Analyser les logs de maintenance",
                "destination": "analyse_logs",
                "condition": None
            },
            "3": {
                "texte": "Retourner au réseau principal",
                "destination": "infiltration_neurocorp",
                "condition": None
            }
        }
    },

    "controle_drone": {
        "id": "controle_drone",
        "titre": "Contrôle du Drone",
        "texte": """
        Vous prenez le contrôle d'un drone de maintenance. À travers ses capteurs,
        vous accédez à des zones sécurisées du réseau de NeuroCorp.
        """,
        "choix": {
            "1": {
                "texte": "Accéder aux serveurs",
                "destination": "decryptage_fichiers",
                "condition": {"intelligence": 7}
            },
            "2": {
                "texte": "Placer des balises",
                "destination": "marquage_guilde",
                "condition": None
            }
        }
    },

    "analyse_logs": {
        "id": "analyse_logs",
        "titre": "Analyse des Logs",
        "texte": """
        Les journaux système révèlent des patterns d'activité suspects. Némésis
        laisse des traces distinctives dans le réseau.
        """,
        "choix": {
            "1": {
                "texte": "Suivre les traces",
                "destination": "decryptage_fichiers",
                "condition": None
            },
            "2": {
                "texte": "Marquer pour la Guilde",
                "destination": "marquage_guilde",
                "condition": None
            }
        }
    },

    "decryptage_fichiers": {
        "id": "decryptage_fichiers",
        "titre": "Secrets Dévoilés",
        "texte": """
        Le décryptage révèle des plans terrifiants. NeuroCorp a utilisé le code
        de Genesis pour créer Némésis, une IA conçue pour manipuler le marché
        des cryptomonnaies. Leur objectif : provoquer un effondrement économique
        et prendre le contrôle du système financier mondial.
        """,
        "choix": {
            "1": {
                "texte": "Télécharger les preuves",
                "destination": "recuperation_preuves",
                "condition": None
            },
            "2": {
                "texte": "Saboter le projet",
                "destination": "sabotage_projet",
                "condition": {"specialisation": "IA & Hacking"}
            },
            "3": {
                "texte": "Alerter la Guilde immédiatement",
                "destination": "alerte_guilde",
                "condition": None
            }
        }
    },

    "recuperation_preuves": {
        "id": "recuperation_preuves",
        "titre": "Course Contre la Montre",
        "texte": """
        Alors que vous téléchargez les fichiers, une alerte de sécurité se déclenche.
        Les systèmes de NeuroCorp ont détecté votre présence. Le temps presse, mais
        les preuves sont cruciales pour stopper Némésis.
        """,
        "choix": {
            "1": {
                "texte": "Accélérer le téléchargement",
                "destination": "acceleration_download",
                "condition": {"intelligence": 7}
            },
            "2": {
                "texte": "Créer une diversion",
                "destination": "diversion_systeme",
                "condition": None
            },
            "3": {
                "texte": "Abandonner le téléchargement",
                "destination": "fuite_urgence",
                "condition": None
            }
        }
    },

    "acceleration_download": {
        "id": "acceleration_download",
        "titre": "Téléchargement Critique",
        "texte": """
        Vous poussez vos implants au maximum, créant des chemins de données
        parallèles. La chaleur monte dans votre cortex neural, mais les fichiers
        s'accumulent rapidement. 95%... 98%... 100% !
        """,
        "choix": {
            "1": {
                "texte": "Se déconnecter rapidement",
                "destination": "extraction_reussie",
                "condition": None
            },
            "2": {
                "texte": "Laisser un virus",
                "destination": "infection_systeme",
                "condition": {"specialisation": "IA & Hacking"}
            }
        }
    },

    "extraction_reussie": {
        "id": "extraction_reussie",
        "titre": "Mission Accomplie",
        "texte": """
        Vous émergez du cyberespace, les preuves en sécurité. Votre tête bourdonne,
        mais vous avez réussi. La Guilde pourra utiliser ces informations pour
        stopper NeuroCorp et Némésis.
        """,
        "choix": {
            "1": {
                "texte": "Contacter la Guilde",
                "destination": "victoire_guilde",
                "condition": None
            }
        }
    },

    "diversion_systeme": {
        "id": "diversion_systeme",
        "titre": "Diversion Système",
        "texte": """
        Vous déclenchez une série d'alertes dans d'autres secteurs du réseau.
        Les équipes de sécurité sont distraites, vous donnant plus de temps.
        """,
        "choix": {
            "1": {
                "texte": "Reprendre le téléchargement",
                "destination": "acceleration_download",
                "condition": None
            },
            "2": {
                "texte": "Fuir pendant la confusion",
                "destination": "fuite_urgence",
                "condition": None
            }
        }
    },

    "fuite_urgence": {
        "id": "fuite_urgence",
        "titre": "Retraite Stratégique",
        "texte": """
        Vous vous déconnectez juste à temps. Les systèmes de sécurité de NeuroCorp
        se referment derrière vous. Vous n'avez pas les preuves, mais vous êtes
        en vie et vous connaissez leur plan.
        """,
        "choix": {
            "1": {
                "texte": "Recommencer une nouvelle partie",
                "destination": "reveil",
                "condition": None
            }
        }
    },

    "sabotage_projet": {
        "id": "sabotage_projet",
        "titre": "Sabotage de Némésis",
        "texte": """
        Vous injectez un code correctif dans Némésis, exploitant une faille que
        vous aviez laissée dans Genesis. L'IA commence à s'auto-désactiver.
        """,
        "choix": {
            "1": {
                "texte": "Compléter la désactivation",
                "destination": "victoire_guilde",
                "condition": None
            },
            "2": {
                "texte": "Prendre le contrôle total",
                "destination": "infection_systeme",
                "condition": {"specialisation": "IA & Hacking"}
            }
        }
    },

    "infection_systeme": {
        "id": "infection_systeme",
        "titre": "Contrôle Total",
        "texte": """
        Vous prenez le contrôle total de Némésis, redirigeant ses capacités pour
        servir la Guilde. Avec cette puissance, vous pouvez rétablir l'équilibre
        économique mondial.
        """,
        "choix": {
            "1": {
                "texte": "Recommencer une nouvelle partie",
                "destination": "reveil",
                "condition": None
            }
        }
    },

    "alerte_guilde": {
        "id": "alerte_guilde",
        "titre": "Alerte à la Guilde",
        "texte": """
        Vous transmettez immédiatement vos découvertes à la Guilde. Leurs experts
        commencent à analyser les données pendant que vous maintenez l'accès.
        """,
        "choix": {
            "1": {
                "texte": "Continuer l'infiltration",
                "destination": "infiltration_neurocorp",
                "condition": None
            },
            "2": {
                "texte": "Coordonner avec la Guilde",
                "destination": "victoire_guilde",
                "condition": None
            }
        }
    },

    "victoire_guilde": {
        "id": "victoire_guilde",
        "titre": "Le Début de la Fin",
        "texte": """
        La Guilde lance immédiatement une opération coordonnée. Les preuves que
        vous avez récupérées sont irréfutables. En quelques heures, les médias
        mondiaux exposent le complot de NeuroCorp. Némésis est isolée et
        désactivée. Vous avez sauvé l'économie mondiale.
        """,
        "choix": {
            "1": {
                "texte": "Recommencer une nouvelle partie",
                "destination": "reveil",
                "condition": None
            }
        }
    },

    "rapport_guilde": {
        "id": "rapport_guilde",
        "titre": "Rapport à la Guilde",
        "texte": """
        Vous transmettez vos découvertes à la Guilde. Les analystes confirment
        vos soupçons : NeuroCorp prépare quelque chose de dangereux.
        """,
        "choix": {
            "1": {
                "texte": "Proposer une infiltration",
                "destination": "preparation_infiltration",
                "condition": None
            },
            "2": {
                "texte": "Retourner sur le terrain",
                "destination": "scan_quartier",
                "condition": None
            }
        }
    },

    "preparation_infiltration": {
        "id": "preparation_infiltration",
        "titre": "Préparation de l'Infiltration",
        "texte": """
        La Guilde met à votre disposition son équipement de pointe. Vous établissez
        un plan d'infiltration détaillé des systèmes de NeuroCorp.
        """,
        "choix": {
            "1": {
                "texte": "Commencer l'infiltration",
                "destination": "infiltration_neurocorp",
                "condition": None
            }
        }
    }
} 