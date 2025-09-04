# Proceedings - Product Search 2024

#### JBNU at TREC 2024 Product Search Track

_Gi-taek An (Jeonbuk National University), Seong-Hyuk Yim (Jeonbuk National University), Jun-Yong Park (Jeonbuk National University), Woo-Seok Choi (Jeonbuk National University), Kyung-Soon Lee (Jeonbuk National University)_

- :fontawesome-solid-user-group: **Participant:** [jbnu](./participants.md#jbnu)
- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec33/papers/jbnu.product.pdf](https://trec.nist.gov/pubs/trec33/papers/jbnu.product.pdf)
- :material-file-search: **Runs:** [jbnu08](./runs.md#jbnu08) | [jbnu04](./runs.md#jbnu04) | [jbnu09](./runs.md#jbnu09) | [jbnu01](./runs.md#jbnu01) | [jbnu07](./runs.md#jbnu07) | [jbnu10](./runs.md#jbnu10) | [jbnu03](./runs.md#jbnu03) | [jbnu02](./runs.md#jbnu02) | [jbnu11](./runs.md#jbnu11) | [jbnu12](./runs.md#jbnu12) | [jbnu05](./runs.md#jbnu05) | [jbnu06](./runs.md#jbnu06)

??? abstract "Abstract"
	
	This paper describes the participation of the jbnu team in the TREC 2024 Product Search Track. This study addresses two key challenges in product search related to sparse and dense retrieval models. For sparse retrieval models, we propose modifying the activation function to GELU to filter out products that, despite being retrieved due to token expansion, are irrelevant for recommendation based on the scoring mechanism. For dense retrieval models, product search document indexing data was generated using the generative model T5 to address input token limitations. Experimental results demonstrate that both proposed methods yield performance improvements over baseline models.
	

??? quote "Bibtex"
	```
	@inproceedings{jbnu-trec2024-papers-proc-1,
		author = {Gi-taek An (Jeonbuk National University), Seong-Hyuk Yim (Jeonbuk National University), Jun-Yong Park (Jeonbuk National University), Woo-Seok Choi (Jeonbuk National University), Kyung-Soon Lee (Jeonbuk National University)},
		title = {JBNU at TREC 2024 Product Search Track},
		booktitle = {The Thirty-Third Text REtrieval Conference Proceedings (TREC 2024), Gaithersburg, MD, USA, November 15-18, 2024},
		series = {NIST Special Publication},
		volume = {1329},
		publisher = {National Institute of Standards and Technology (NIST)},
		year = {2024},
		trec_org = {jbnu},
		trec_runs = {jbnu08, jbnu04, jbnu09, jbnu01, jbnu07, jbnu10, jbnu03, jbnu02, jbnu11, jbnu12, jbnu05, jbnu06},
		trec_tracks = {product},
		url = {https://trec.nist.gov/pubs/trec33/papers/jbnu.product.pdf}
	}
	```

