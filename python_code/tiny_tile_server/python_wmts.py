
import bottle
import python_server.py

def get_tile_wmts(layer):

	python_wmts = bottle.Bottle();

	maps = maps();

	bottle.response.content_type = "application/xml"

	print "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
	<Capabilities xmlns="http://www.opengis.net/wmts/1.0" xmlns:ows="http://www.opengis.net/ows/1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gml="http://www.opengis.net/gml" xsi:schemaLocation="http://www.opengis.net/wmts/1.0 http://schemas.opengis.net/wmts/1.0/wmtsGetCapabilities_response.xsd" version="1.0.0">
	  <!-- Service Identification -->
	  <ows:ServiceIdentification>
		<ows:Title>Tiny Tile Server</ows:Title>
		<ows:ServiceType>OGC WMTS</ows:ServiceType>
		<ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
	  </ows:ServiceIdentification>
	  <!-- Operations Metadata -->
	  <ows:OperationsMetadata>
		<ows:Operation name="GetCapabilities">
		  <ows:DCP>
			<ows:HTTP>
			  <ows:Get xlink:href="<% print config_url[0] %>wmts/1.0.0/WMTSCapabilities.xml">
				<ows:Constraint name="GetEncoding">
				  <ows:AllowedValues>
					<ows:Value>RESTful</ows:Value>
				  </ows:AllowedValues>
				</ows:Constraint>
			  </ows:Get>
			  <!-- add KVP binding in 10.1 -->
			  <ows:Get xlink:href="<% print config_url[0] %>wmts?">
				<ows:Constraint name="GetEncoding">
				  <ows:AllowedValues>
					<ows:Value>KVP</ows:Value>
				  </ows:AllowedValues>
				</ows:Constraint>
			  </ows:Get>
			</ows:HTTP>
		  </ows:DCP>
		</ows:Operation>
		<ows:Operation name="GetTile">
		  <ows:DCP>
			<ows:HTTP>
			  <ows:Get xlink:href="<% print config_url[0] %>wmts/">
				<ows:Constraint name="GetEncoding">
				  <ows:AllowedValues>
					<ows:Value>RESTful</ows:Value>
				  </ows:AllowedValues>
				</ows:Constraint>
			  </ows:Get>
			  <ows:Get xlink:href="<% print config_url[0] %>wmts?">
				<ows:Constraint name="GetEncoding">
				  <ows:AllowedValues>
					<ows:Value>KVP</ows:Value>
				  </ows:AllowedValues>
				</ows:Constraint>
			  </ows:Get>
			</ows:HTTP>
		  </ows:DCP>
		</ows:Operation>
	  </ows:OperationsMetadata>
	  <Contents>

	<%
	for m in maps:
		basename = m['basename'];
		title = m['name'] if ('name' in m) else basename;
		profile = m['profile'];
		bounds = m['bounds'];
		format = m['format'];
		mime = 'image/jpeg' if (format == 'jpg') else 'image/png';
		if (profile == 'geodetic'):
			tileMatrixSet = "WGS84"
		else:
			tileMatrixSet = "GoogleMapsCompatible"
			(minx, miny) = mercator.LatLonToMeters(bounds[1], bounds[0]);
			(maxx, maxy) = mercator.LatLonToMeters(bounds[3], bounds[2]);
			bounds3857 = array(minx, miny, maxx, maxy);
	%>

		<Layer>
		  <ows:Title><% print title %></ows:Title>
		  <ows:Identifier><% print basename %></ows:Identifier>
		  <ows:WGS84BoundingBox crs="urn:ogc:def:crs:OGC:2:84">
			<ows:LowerCorner><% print bounds[0], ' ', bounds[1] %></ows:LowerCorner>
			<ows:UpperCorner><% print bounds[2], ' ', bounds[3] %></ows:UpperCorner>
		  </ows:WGS84BoundingBox>
		  <Style isDefault="true">
			<ows:Identifier>default</ows:Identifier>
		  </Style>
		  <Format><% print mime %></Format>
		  <TileMatrixSetLink>
			<TileMatrixSet><% print tileMatrixSet %></TileMatrixSet>
		  </TileMatrixSetLink>
		  <ResourceURL format="<% print mime %>" resourceType="tile" template="<% print config_url[0] %><% print basename %>/{TileMatrixSet}/{TileMatrix}/{TileCol}/{TileRow}.<% print format %>"/>
		</Layer>
		
		<!--TileMatrixSet-->

		<TileMatrixSet>
		  <ows:Title>GoogleMapsCompatible</ows:Title>
		  <ows:Abstract>the wellknown 'GoogleMapsCompatible' tile matrix set defined by OGC WMTS specification</ows:Abstract>
		  <ows:Identifier>GoogleMapsCompatible</ows:Identifier>
		  <ows:SupportedCRS>urn:ogc:def:crs:EPSG:6.18:3:3857</ows:SupportedCRS>
		  <WellKnownScaleSet>urn:ogc:def:wkss:OGC:1.0:GoogleMapsCompatible</WellKnownScaleSet>
		  <TileMatrix>
			<ows:Identifier>0</ows:Identifier>
			<ScaleDenominator>559082264.0287178</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>1</MatrixWidth>
			<MatrixHeight>1</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>1</ows:Identifier>
			<ScaleDenominator>279541132.0143589</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>2</MatrixWidth>
			<MatrixHeight>2</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>2</ows:Identifier>
			<ScaleDenominator>139770566.0071794</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>4</MatrixWidth>
			<MatrixHeight>4</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>3</ows:Identifier>
			<ScaleDenominator>69885283.00358972</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>8</MatrixWidth>
			<MatrixHeight>8</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>4</ows:Identifier>
			<ScaleDenominator>34942641.50179486</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>16</MatrixWidth>
			<MatrixHeight>16</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>5</ows:Identifier>
			<ScaleDenominator>17471320.75089743</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>32</MatrixWidth>
			<MatrixHeight>32</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>6</ows:Identifier>
			<ScaleDenominator>8735660.375448715</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>64</MatrixWidth>
			<MatrixHeight>64</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>7</ows:Identifier>
			<ScaleDenominator>4367830.187724357</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>128</MatrixWidth>
			<MatrixHeight>128</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>8</ows:Identifier>
			<ScaleDenominator>2183915.093862179</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>256</MatrixWidth>
			<MatrixHeight>256</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>9</ows:Identifier>
			<ScaleDenominator>1091957.546931089</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>512</MatrixWidth>
			<MatrixHeight>512</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>10</ows:Identifier>
			<ScaleDenominator>545978.7734655447</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>1024</MatrixWidth>
			<MatrixHeight>1024</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>11</ows:Identifier>
			<ScaleDenominator>272989.3867327723</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>2048</MatrixWidth>
			<MatrixHeight>2048</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>12</ows:Identifier>
			<ScaleDenominator>136494.6933663862</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>4096</MatrixWidth>
			<MatrixHeight>4096</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>13</ows:Identifier>
			<ScaleDenominator>68247.34668319309</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>8192</MatrixWidth>
			<MatrixHeight>8192</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>14</ows:Identifier>
			<ScaleDenominator>34123.67334159654</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>16384</MatrixWidth>
			<MatrixHeight>16384</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>15</ows:Identifier>
			<ScaleDenominator>17061.83667079827</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>32768</MatrixWidth>
			<MatrixHeight>32768</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>16</ows:Identifier>
			<ScaleDenominator>8530.918335399136</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>65536</MatrixWidth>
			<MatrixHeight>65536</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>17</ows:Identifier>
			<ScaleDenominator>4265.459167699568</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>131072</MatrixWidth>
			<MatrixHeight>131072</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>18</ows:Identifier>
			<ScaleDenominator>2132.729583849784</ScaleDenominator>
			<TopLeftCorner>-20037508.34278925 20037508.34278925</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>262144</MatrixWidth>
			<MatrixHeight>262144</MatrixHeight>
		  </TileMatrix>
		</TileMatrixSet>

		<TileMatrixSet>
		  <ows:Identifier>WGS84</ows:Identifier>
		  <ows:Title>GoogleCRS84Quad</ows:Title>
		  <ows:SupportedCRS>urn:ogc:def:crs:EPSG:6.3:4326</ows:SupportedCRS>
		  <ows:BoundingBox crs="urn:ogc:def:crs:EPSG:6.3:4326">
			<LowerCorner>-180.000000 -90.000000</LowerCorner>
			<UpperCorner>180.000000 90.000000</UpperCorner>
		  </ows:BoundingBox>
		  <WellKnownScaleSet>urn:ogc:def:wkss:OGC:1.0:GoogleCRS84Quad</WellKnownScaleSet>
		  <TileMatrix>
			<ows:Identifier>0</ows:Identifier>
			<ScaleDenominator>279541132.01435887813568115234</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>2</MatrixWidth>
			<MatrixHeight>1</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>1</ows:Identifier>
			<ScaleDenominator>139770566.00717943906784057617</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>4</MatrixWidth>
			<MatrixHeight>2</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>2</ows:Identifier>
			<ScaleDenominator>69885283.00358971953392028809</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>8</MatrixWidth>
			<MatrixHeight>4</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>3</ows:Identifier>
			<ScaleDenominator>34942641.50179485976696014404</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>16</MatrixWidth>
			<MatrixHeight>8</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>4</ows:Identifier>
			<ScaleDenominator>17471320.75089742988348007202</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>32</MatrixWidth>
			<MatrixHeight>16</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>5</ows:Identifier>
			<ScaleDenominator>8735660.37544871494174003601</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>64</MatrixWidth>
			<MatrixHeight>32</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>6</ows:Identifier>
			<ScaleDenominator>4367830.18772435747087001801</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>128</MatrixWidth>
			<MatrixHeight>64</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>7</ows:Identifier>
			<ScaleDenominator>2183915.09386217873543500900</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>256</MatrixWidth>
			<MatrixHeight>128</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>8</ows:Identifier>
			<ScaleDenominator>1091957.54693108936771750450</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>512</MatrixWidth>
			<MatrixHeight>256</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>9</ows:Identifier>
			<ScaleDenominator>545978.77346554468385875225</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>1024</MatrixWidth>
			<MatrixHeight>512</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>10</ows:Identifier>
			<ScaleDenominator>272989.38673277234192937613</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>2048</MatrixWidth>
			<MatrixHeight>1024</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>11</ows:Identifier>
			<ScaleDenominator>136494.69336638617096468806</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>4096</MatrixWidth>
			<MatrixHeight>2048</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>12</ows:Identifier>
			<ScaleDenominator>68247.34668319308548234403</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>8192</MatrixWidth>
			<MatrixHeight>4096</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>13</ows:Identifier>
			<ScaleDenominator>34123.67334159654274117202</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>16384</MatrixWidth>
			<MatrixHeight>8192</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>14</ows:Identifier>
			<ScaleDenominator>17061.83667079825318069197</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>32768</MatrixWidth>
			<MatrixHeight>16384</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>15</ows:Identifier>
			<ScaleDenominator>8530.91833539912659034599</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>65536</MatrixWidth>
			<MatrixHeight>32768</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>16</ows:Identifier>
			<ScaleDenominator>4265.45916769956329517299</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>131072</MatrixWidth>
			<MatrixHeight>65536</MatrixHeight>
		  </TileMatrix>
		  <TileMatrix>
			<ows:Identifier>17</ows:Identifier>
			<ScaleDenominator>2132.72958384978574031265</ScaleDenominator>
			<TopLeftCorner>90.000000 -180.000000</TopLeftCorner>
			<TileWidth>256</TileWidth>
			<TileHeight>256</TileHeight>
			<MatrixWidth>262144</MatrixWidth>
			<MatrixHeight>131072</MatrixHeight>
		  </TileMatrix>
		</TileMatrixSet>

	  </Contents>
	  <ServiceMetadataURL xlink:href="<% print config_url[0] %>wmts/1.0.0/WMTSCapabilities.xml"/>
	</Capabilities>